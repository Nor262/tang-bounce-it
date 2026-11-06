using UnityEngine;

namespace JegiOdyssey
{
    public class JegiAudioManager : MonoBehaviour
    {
        [Header("Audio Sources")]
        public AudioSource SfxSource;
        public AudioSource MusicSource;

        [Header("Audio Clips")]
        public AudioClip NormalKickClip;
        public AudioClip PerfectKickClip;
        public AudioClip WhiffClip;
        public AudioClip LevelUpClip;
        public AudioClip GameOverClip;
        public AudioClip DdakjiButtonClickClip;

        public void PlayKickSound(bool isPerfect)
        {
            if (SfxSource == null) return;
            AudioClip clip = isPerfect ? (PerfectKickClip != null ? PerfectKickClip : NormalKickClip) : NormalKickClip;
            if (clip != null)
            {
                SfxSource.pitch = isPerfect ? Random.Range(1.1f, 1.25f) : Random.Range(0.95f, 1.05f);
                SfxSource.PlayOneShot(clip);
            }
        }

        public void PlayWhiffSound()
        {
            if (SfxSource != null && WhiffClip != null)
            {
                SfxSource.pitch = Random.Range(0.9f, 1.1f);
                SfxSource.PlayOneShot(WhiffClip);
            }
        }

        public void PlayLevelUpSound()
        {
            if (SfxSource != null && LevelUpClip != null)
            {
                SfxSource.pitch = 1.0f;
                SfxSource.PlayOneShot(LevelUpClip);
            }
        }

        public void PlayGameOverSound()
        {
            if (SfxSource != null && GameOverClip != null)
            {
                SfxSource.pitch = 1.0f;
                SfxSource.PlayOneShot(GameOverClip);
            }
        }

        public void PlayButtonClick()
        {
            if (SfxSource != null && DdakjiButtonClickClip != null)
            {
                SfxSource.pitch = Random.Range(0.95f, 1.05f);
                SfxSource.PlayOneShot(DdakjiButtonClickClip);
            }
        }
    }
}
