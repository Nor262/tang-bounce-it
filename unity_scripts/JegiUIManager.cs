using System.Collections;
using UnityEngine;
using UnityEngine.UI;

namespace JegiOdyssey
{
    public class JegiUIManager : MonoBehaviour
    {
        [Header("Screens")]
        public GameObject MainMenuPanel;
        public GameObject InGameHUDPanel;
        public GameObject GameOverPanel;
        public GameObject WorkshopPanel;

        [Header("HUD Text Elements")]
        public Text CurrentScoreText;
        public Text BestScoreHUDText;
        public Text LevelIndicatorText;
        public Text WindIndicatorText;
        public Text ComboToastText;

        [Header("Game Over Elements")]
        public Text FinalScoreText;
        public Text BestScoreGameOverText;
        public Text LevelReachedText;
        public GameObject NewRecordBadge;
        public Text CulturalTriviaText;

        [Header("Buttons (Ddakji styled)")]
        public Button PlayButton;
        public Button RetryButton;
        public Button WorkshopButton;
        public Button CloseWorkshopButton;

        private Coroutine comboCoroutine;

        private void Awake()
        {
            if (PlayButton != null) PlayButton.onClick.AddListener(OnPlayClicked);
            if (RetryButton != null) RetryButton.onClick.AddListener(OnRetryClicked);
            if (WorkshopButton != null) WorkshopButton.onClick.AddListener(OnWorkshopClicked);
            if (CloseWorkshopButton != null) CloseWorkshopButton.onClick.AddListener(OnCloseWorkshopClicked);
        }

        public void OnGameStateChanged(GameState state)
        {
            MainMenuPanel.SetActive(state == GameState.MainMenu);
            InGameHUDPanel.SetActive(state == GameState.Playing);
            GameOverPanel.SetActive(state == GameState.GameOver);
        }

        public void UpdateHUD(int score, int level, int combo, float wind)
        {
            if (CurrentScoreText != null) CurrentScoreText.text = score.ToString();
            if (BestScoreHUDText != null) BestScoreHUDText.text = JegiGameManager.Instance.BestScore.ToString();
            if (LevelIndicatorText != null) LevelIndicatorText.text = $"CẤP {level}/5";

            if (WindIndicatorText != null)
            {
                if (Mathf.Abs(wind) < 0.1f)
                {
                    WindIndicatorText.text = "Gió: Lặng";
                }
                else
                {
                    string arrow = wind > 0 ? ">>" : "<<";
                    WindIndicatorText.text = $"Gió: {arrow} {Mathf.Abs(wind):F1} m/s";
                }
            }

            if (combo >= 2)
            {
                ShowComboToast($"{combo}x THẦN SẦU!");
            }
        }

        public void ShowComboToast(string text)
        {
            if (ComboToastText == null) return;
            if (comboCoroutine != null) StopCoroutine(comboCoroutine);
            comboCoroutine = StartCoroutine(AnimateComboToast(text));
        }

        private IEnumerator AnimateComboToast(string text)
        {
            ComboToastText.gameObject.SetActive(true);
            ComboToastText.text = text;
            ComboToastText.transform.localScale = Vector3.one * 1.3f;

            float t = 0f;
            while (t < 0.2f)
            {
                t += Time.deltaTime;
                yield return null;
            }
            ComboToastText.transform.localScale = Vector3.one;

            yield return new WaitForSeconds(0.6f);
            ComboToastText.gameObject.SetActive(false);
        }

        public void ShowLevelUpBanner(int newLevel)
        {
            string[] levelNames = {
                "Sân Đình Làng Bắc Bộ",
                "Phố Cổ Hội An Đêm Đèn Lồng",
                "Giao Lộ Hạ Long & Đảo Jeju",
                "Làng Cổ Bukchon Hanok Mùa Thu",
                "Hoàng Cung Gyeongbokgung Đêm Tuyết"
            };

            string name = (newLevel >= 1 && newLevel <= 5) ? levelNames[newLevel - 1] : "";
            ShowComboToast($"TIẾN VÀO: {name.ToUpper()}!");
        }

        public void ShowFeverBanner(bool active)
        {
            if (active)
            {
                ShowComboToast("★ FEVER MODE: TÂNG ĐÔI ĐIỂM! ★");
            }
        }

        public void ShowGameOverScreen(int finalScore, int bestScore, int level, bool isNewRecord)
        {
            if (FinalScoreText != null) FinalScoreText.text = finalScore.ToString();
            if (BestScoreGameOverText != null) BestScoreGameOverText.text = bestScore.ToString();
            if (LevelReachedText != null) LevelReachedText.text = $"CẤP ĐỘ ĐẠT ĐƯỢC: {level}/5";
            if (NewRecordBadge != null) NewRecordBadge.SetActive(isNewRecord);

            string[] trivias = {
                "Bạn có biết? Jegichagi truyền thống Hàn Quốc có luật vượt qua 5 cấp độ kỹ thuật chân!",
                "Quả cầu Jegi và quả cầu đá Việt Nam đều sử dụng đồng xu bọc vải để hạ thấp trọng tâm.",
                "Trò chơi Đá cầu và Jegichagi đều là di sản gắn kết cộng đồng dịp Tết Seollal và Tết Nguyên Đán."
            };

            if (CulturalTriviaText != null)
            {
                CulturalTriviaText.text = trivias[Random.Range(0, trivias.Length)];
            }
        }

        private void OnPlayClicked()
        {
            JegiGameManager.Instance.StartGame();
        }

        private void OnRetryClicked()
        {
            JegiGameManager.Instance.StartGame();
        }

        private void OnWorkshopClicked()
        {
            if (WorkshopPanel != null) WorkshopPanel.SetActive(true);
        }

        private void OnCloseWorkshopClicked()
        {
            if (WorkshopPanel != null) WorkshopPanel.SetActive(false);
        }
    }
}
