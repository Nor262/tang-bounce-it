using System;
using UnityEngine;

namespace JegiOdyssey
{
    public enum GameState
    {
        MainMenu,
        Playing,
        GameOver
    }

    public class JegiGameManager : MonoBehaviour
    {
        public static JegiGameManager Instance { get; private set; }

        [Header("Game State")]
        public GameState CurrentState = GameState.MainMenu;

        [Header("Score & Progress")]
        public int CurrentScore = 0;
        public int BestScore = 0;
        public int CurrentLevel = 1; // 1 to 5 stages
        public int ConsecutiveCombo = 0;
        public int TotalCoins = 0;

        [Header("Fever Mode")]
        public float FeverMeter = 0f;
        public bool IsFeverActive = false;
        private float feverDuration = 5f;
        private float feverTimer = 0f;

        [Header("Wind Mechanics")]
        public float CurrentWindForce = 0f; // negative: left, positive: right

        [Header("References")]
        public JegiShuttlecock Shuttlecock;
        public JegiPlayerController Player;
        public JegiUIManager UIManager;
        public JegiAudioManager AudioManager;

        private const string BEST_SCORE_KEY = "KGW_JEGI_BEST_SCORE";
        private const string COINS_KEY = "KGW_JEGI_COINS";

        private void Awake()
        {
            if (Instance == null)
            {
                Instance = this;
            }
            else
            {
                Destroy(gameObject);
                return;
            }

            BestScore = PlayerPrefs.GetInt(BEST_SCORE_KEY, 0);
            TotalCoins = PlayerPrefs.GetInt(COINS_KEY, 0);
        }

        private void Start()
        {
            SetState(GameState.MainMenu);
        }

        private void Update()
        {
            if (CurrentState == GameState.Playing)
            {
                // Handle Fever Timer
                if (IsFeverActive)
                {
                    feverTimer -= Time.deltaTime;
                    if (feverTimer <= 0f)
                    {
                        EndFeverMode();
                    }
                }
            }
        }

        public void StartGame()
        {
            CurrentScore = 0;
            ConsecutiveCombo = 0;
            CurrentLevel = 1;
            FeverMeter = 0f;
            IsFeverActive = false;
            CurrentWindForce = 0f;

            SetState(GameState.Playing);

            if (Shuttlecock != null)
            {
                Shuttlecock.SpawnAndServe();
            }

            if (UIManager != null)
            {
                UIManager.UpdateHUD(CurrentScore, CurrentLevel, ConsecutiveCombo, CurrentWindForce);
            }
        }

        public void AddScore(int points, bool isPerfect)
        {
            CurrentScore += points;

            if (isPerfect)
            {
                ConsecutiveCombo++;
                FeverMeter = Mathf.Clamp01(FeverMeter + 0.15f);
                if (FeverMeter >= 1f && !IsFeverActive)
                {
                    StartFeverMode();
                }
            }
            else
            {
                ConsecutiveCombo = 0;
            }

            // Coin reward (1 coin per 5 kicks)
            if (CurrentScore % 5 == 0)
            {
                TotalCoins++;
                PlayerPrefs.SetInt(COINS_KEY, TotalCoins);
            }

            // Level Progression (5 stages)
            CheckLevelProgression();

            if (UIManager != null)
            {
                UIManager.UpdateHUD(CurrentScore, CurrentLevel, ConsecutiveCombo, CurrentWindForce);
            }
        }

        private void CheckLevelProgression()
        {
            int previousLevel = CurrentLevel;

            if (CurrentScore >= 90) CurrentLevel = 5;      // Gyeongbokgung Snow
            else if (CurrentScore >= 61) CurrentLevel = 4; // Bukchon Autumn
            else if (CurrentScore >= 36) CurrentLevel = 3; // Ha Long & Jeju
            else if (CurrentScore >= 16) CurrentLevel = 2; // Hoi An Lantern
            else CurrentLevel = 1;                         // Dinh Lang Village

            if (CurrentLevel > previousLevel)
            {
                OnLevelUp();
            }

            // Dynamic Wind update based on Level
            UpdateWindByLevel();
        }

        private void UpdateWindByLevel()
        {
            if (IsFeverActive)
            {
                CurrentWindForce = 0f;
                return;
            }

            switch (CurrentLevel)
            {
                case 1:
                    CurrentWindForce = 0f;
                    break;
                case 2:
                    CurrentWindForce = -1.2f; // Mild breeze from right to left
                    break;
                case 3:
                    // Random ocean breeze changing every few kicks
                    if (CurrentScore % 5 == 0)
                    {
                        CurrentWindForce = UnityEngine.Random.Range(-3f, 3f);
                    }
                    break;
                case 4:
                    CurrentWindForce = UnityEngine.Random.Range(-4f, 4f);
                    break;
                case 5:
                    CurrentWindForce = UnityEngine.Random.Range(-6f, 6f);
                    break;
            }
        }

        private void OnLevelUp()
        {
            if (AudioManager != null)
            {
                AudioManager.PlayLevelUpSound();
            }

            if (UIManager != null)
            {
                UIManager.ShowLevelUpBanner(CurrentLevel);
            }
        }

        private void StartFeverMode()
        {
            IsFeverActive = true;
            feverTimer = feverDuration;
            CurrentWindForce = 0f;

            if (UIManager != null)
            {
                UIManager.ShowFeverBanner(true);
            }
        }

        private void EndFeverMode()
        {
            IsFeverActive = false;
            FeverMeter = 0f;

            if (UIManager != null)
            {
                UIManager.ShowFeverBanner(false);
            }
        }

        public void TriggerGameOver()
        {
            if (CurrentState == GameState.GameOver) return;

            SetState(GameState.GameOver);

            bool isNewRecord = false;
            if (CurrentScore > BestScore)
            {
                BestScore = CurrentScore;
                PlayerPrefs.SetInt(BEST_SCORE_KEY, BestScore);
                PlayerPrefs.Save();
                isNewRecord = true;
            }

            if (AudioManager != null)
            {
                AudioManager.PlayGameOverSound();
            }

            if (UIManager != null)
            {
                UIManager.ShowGameOverScreen(CurrentScore, BestScore, CurrentLevel, isNewRecord);
            }
        }

        public void SetState(GameState newState)
        {
            CurrentState = newState;
            if (UIManager != null)
            {
                UIManager.OnGameStateChanged(newState);
            }
        }
    }
}
