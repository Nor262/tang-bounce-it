using UnityEngine;

namespace JegiOdyssey
{
    [CreateAssetMenu(fileName = "NewJegiSkin", menuName = "JegiOdyssey/Skin Data")]
    public class JegiSkinData : ScriptableObject
    {
        [Header("Skin Metadata")]
        public string SkinId;
        public string SkinName;
        [TextArea(2, 4)]
        public string CulturalDescription;
        public Sprite SkinIcon;
        public int UnlockCoinCost = 0;
        public bool IsUnlockedByDefault = false;

        [Header("Physics Modifiers")]
        [Tooltip("Multiplies the base mass (m = 1.0)")]
        public float MassMultiplier = 1.0f;

        [Tooltip("Multiplies the upward bounce force")]
        public float BounceMultiplier = 1.0f;

        [Tooltip("0 = no resistance, 0.5 = 50% resistance to wind")]
        [Range(0f, 1f)]
        public float WindResistanceFactor = 0f;

        [Tooltip("Visual Trail Color for ribbons")]
        public Color RibbonTrailColor = Color.yellow;
    }
}
