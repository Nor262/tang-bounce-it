using UnityEngine;

namespace JegiOdyssey
{
    public class JegiPlayerController : MonoBehaviour
    {
        [Header("Character Properties")]
        public string CharacterName = "Bé Nam"; // or "Bé Ji-ho"
        public Transform FootKickTransform;     // Pivot of the kicking foot
        public Transform TargetRingTransform;    // Visual target ring on the ground

        [Header("Hit-Zone Thresholds (meters)")]
        public float PerfectThresholdX = 0.25f;
        public float GreatThresholdX = 0.55f;
        public float GrazeThresholdX = 0.95f;
        public float MaxVerticalHitDistance = 0.6f;

        [Header("Animations & Sprites")]
        public Animator CharacterAnimator;
        public SpriteRenderer FacialExpressionRenderer;
        public Sprite FaceNormal;
        public Sprite FaceConfident;
        public Sprite FaceWorried;
        public Sprite FaceCryFail;

        [Header("References")]
        public JegiShuttlecock Shuttlecock;

        private Camera mainCamera;
        private bool isAlternateLeg = false;

        private void Start()
        {
            mainCamera = Camera.main;
            SetFacialExpression(FaceNormal);
        }

        private void Update()
        {
            if (JegiGameManager.Instance == null || JegiGameManager.Instance.CurrentState != GameState.Playing)
            {
                return;
            }

            HandleDynamicFacialExpression();
            HandlePlayerInput();
        }

        private void HandlePlayerInput()
        {
            // One-tap input: Touch on mobile or Left Click / Space on PC
            bool inputTriggered = false;
            Vector3 worldInputPos = Vector3.zero;

            if (Input.GetMouseButtonDown(0))
            {
                inputTriggered = true;
                worldInputPos = mainCamera.ScreenToWorldPoint(Input.mousePosition);
            }
            else if (Input.touchCount > 0 && Input.GetTouch(0).phase == TouchPhase.Began)
            {
                inputTriggered = true;
                worldInputPos = mainCamera.ScreenToWorldPoint(Input.GetTouch(0).position);
            }
            else if (Input.GetKeyDown(KeyCode.Space))
            {
                inputTriggered = true;
                worldInputPos = FootKickTransform.position;
            }

            if (inputTriggered)
            {
                ExecuteKickAttempt(worldInputPos.x);
            }
        }

        private void ExecuteKickAttempt(float inputWorldX)
        {
            if (Shuttlecock == null) return;

            // Trigger visual kicking animation
            TriggerKickAnimation();

            // Check distance between shuttlecock and kick point
            Vector3 jegiPos = Shuttlecock.transform.position;
            Vector3 footPos = FootKickTransform.position;

            float deltaX = jegiPos.x - inputWorldX;
            float absDeltaX = Mathf.Abs(jegiPos.x - footPos.x);
            float distY = Mathf.Abs(jegiPos.y - footPos.y);

            // Check if shuttlecock is falling and in the vertical reach zone
            Rigidbody2D rb = Shuttlecock.GetComponent<Rigidbody2D>();
            bool isFalling = rb != null && rb.velocity.y <= 0.5f;

            if (distY <= MaxVerticalHitDistance && absDeltaX <= GrazeThresholdX && isFalling)
            {
                // Successful Hit!
                bool isPerfect = absDeltaX <= PerfectThresholdX && distY <= 0.35f;
                bool isGreat = !isPerfect && absDeltaX <= GreatThresholdX;

                int points = isPerfect ? 3 : (isGreat ? 2 : 1);
                float timingFactor = isPerfect ? 1.15f : (isGreat ? 1.0f : 0.85f);

                Shuttlecock.ApplyKickImpulse(deltaX, timingFactor, isPerfect);

                if (JegiGameManager.Instance != null)
                {
                    JegiGameManager.Instance.AddScore(points, isPerfect);
                }

                if (JegiGameManager.Instance != null && JegiGameManager.Instance.AudioManager != null)
                {
                    JegiGameManager.Instance.AudioManager.PlayKickSound(isPerfect);
                }

                // Temporary happy/confident expression
                SetFacialExpression(FaceConfident);
                Invoke(nameof(ResetFacialExpression), 0.4f);
            }
            else
            {
                // Whiff / Early Kick into empty air
                if (JegiGameManager.Instance != null && JegiGameManager.Instance.AudioManager != null)
                {
                    JegiGameManager.Instance.AudioManager.PlayWhiffSound();
                }
            }
        }

        private void TriggerKickAnimation()
        {
            isAlternateLeg = !isAlternateLeg;

            if (CharacterAnimator != null)
            {
                CharacterAnimator.SetTrigger(isAlternateLeg ? "KickRight" : "KickLeft");
            }
        }

        private void HandleDynamicFacialExpression()
        {
            if (Shuttlecock == null) return;

            float jegiHeight = Shuttlecock.transform.position.y;
            float footHeight = FootKickTransform.position.y;

            if (jegiHeight - footHeight < 0.35f)
            {
                SetFacialExpression(FaceWorried);
            }
        }

        public void SetFacialExpression(Sprite expressionSprite)
        {
            if (FacialExpressionRenderer != null && expressionSprite != null)
            {
                FacialExpressionRenderer.sprite = expressionSprite;
            }
        }

        private void ResetFacialExpression()
        {
            SetFacialExpression(FaceNormal);
        }
    }
}
