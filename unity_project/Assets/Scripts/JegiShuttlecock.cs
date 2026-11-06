using UnityEngine;

namespace JegiOdyssey
{
    [RequireComponent(typeof(Rigidbody2D))]
    [RequireComponent(typeof(CircleCollider2D))]
    public class JegiShuttlecock : MonoBehaviour
    {
        [Header("Physics Constants")]
        public float BaseMass = 1.0f;
        public float UpwardForce = 12.0f;
        public float HorizontalSensitivity = 5.0f;
        public float AerodynamicAirDrag = 0.985f;
        public float AngularDamping = 0.92f;

        [Header("Current Active Skin")]
        public JegiSkinData ActiveSkin;

        [Header("Visual Elements")]
        public Transform CoinBaseTransform;
        public TrailRenderer RibbonTrail;
        public ParticleSystem HitSparkParticles;

        private Rigidbody2D rb;
        private CircleCollider2D col;
        private bool isGrounded = false;

        private void Awake()
        {
            rb = GetComponent<Rigidbody2D>();
            col = GetComponent<CircleCollider2D>();
            ApplySkin(ActiveSkin);
        }

        public void ApplySkin(JegiSkinData skin)
        {
            if (skin == null) return;
            ActiveSkin = skin;
            rb.mass = BaseMass * skin.MassMultiplier;
            // Additional visual modifications can be bound here
        }

        public void SpawnAndServe()
        {
            isGrounded = false;
            transform.position = new Vector3(0f, 1.8f, 0f);
            rb.velocity = new Vector2(0f, 1.5f);
            rb.angularVelocity = 0f;
            rb.gravityScale = 2.4f;

            if (RibbonTrail != null)
            {
                RibbonTrail.Clear();
                RibbonTrail.enabled = true;
            }
        }

        private void FixedUpdate()
        {
            if (JegiGameManager.Instance == null || JegiGameManager.Instance.CurrentState != GameState.Playing)
            {
                return;
            }

            // Apply Wind Force
            float wind = JegiGameManager.Instance.CurrentWindForce;
            if (ActiveSkin != null)
            {
                wind *= (1f - ActiveSkin.WindResistanceFactor);
            }
            rb.AddForce(new Vector2(wind * 1.8f, 0f));

            // Aerodynamic Drag on Tassels / Ribbons
            rb.velocity = new Vector2(rb.velocity.x * AerodynamicAirDrag, rb.velocity.y);

            // Natural shuttlecock orientation: Heavy coin heads downward when falling
            if (rb.velocity.y < -0.5f)
            {
                float targetAngle = Mathf.Atan2(rb.velocity.y, rb.velocity.x) * Mathf.Rad2Deg + 90f;
                float currentAngle = rb.rotation;
                rb.rotation = Mathf.LerpAngle(currentAngle, targetAngle, Time.fixedDeltaTime * 4f);
            }
        }

        /// <summary>
        /// Applies impulse force when kicked by player.
        /// deltaX = x_jegi - x_input
        /// </summary>
        public void ApplyKickImpulse(float deltaX, float verticalTimingFactor, bool isPerfect)
        {
            // Reset vertical momentum to ensure responsive bounce
            rb.velocity = Vector2.zero;

            float horizontalImpulse = deltaX * HorizontalSensitivity;
            float verticalImpulse = UpwardForce * verticalTimingFactor;

            // Extra bounce if skin has bounce bonus
            if (ActiveSkin != null)
            {
                verticalImpulse *= ActiveSkin.BounceMultiplier;
            }

            Vector2 kickVector = new Vector2(horizontalImpulse, verticalImpulse);
            rb.AddForce(kickVector, ForceMode2D.Impulse);

            // Random subtle angular spin
            float spin = -deltaX * 350f;
            rb.angularVelocity = spin;

            // Particle sparks
            if (HitSparkParticles != null)
            {
                HitSparkParticles.transform.position = transform.position;
                HitSparkParticles.Play();
            }

            // Squash and stretch effect
            StopAllCoroutines();
            StartCoroutine(SquashAndStretchCoroutine());
        }

        private System.Collections.IEnumerator SquashAndStretchCoroutine()
        {
            Vector3 originalScale = Vector3.one;
            Vector3 squashedScale = new Vector3(1.3f, 0.7f, 1f);

            transform.localScale = squashedScale;
            yield return new WaitForSeconds(0.06f);

            float t = 0f;
            while (t < 1f)
            {
                t += Time.deltaTime * 12f;
                transform.localScale = Vector3.Lerp(squashedScale, originalScale, t);
                yield return null;
            }
            transform.localScale = originalScale;
        }

        private void OnCollisionEnter2D(Collision2D collision)
        {
            if (collision.gameObject.CompareTag("Ground") && !isGrounded)
            {
                isGrounded = true;
                rb.velocity = Vector2.zero;
                rb.gravityScale = 0f;

                if (RibbonTrail != null)
                {
                    RibbonTrail.enabled = false;
                }

                if (JegiGameManager.Instance != null)
                {
                    JegiGameManager.Instance.TriggerGameOver();
                }
            }
        }
    }
}
