using TMPro;
using UnityEngine;
using UnityEngine.UI;

[CreateAssetMenu(fileName = "StatCard", menuName = "StatCard")]
public class StatCard : ScriptableObject
{
    public string statName;
    public Texture icon;
    public int maxValue;

    [Header("Normal value")]
    public int defaultvalue;

    [Header("UI Stuff")]
    public Texture backPanel;
    public Texture valueBackground;
}

public class StatCardManager : MonoBehaviour{
    [SerializeField] private StatCard card;

    [Header("Actual Objects")]
    [SerializeField] private RawImage icon;
    [SerializeField] private RawImage backPanel;
    [SerializeField] private RawImage valueBackground;
    [SerializeField] private TMP_Text label;
    [SerializeField] private TMP_Text valueText;

    [Header("If Slider")]
    [SerializeField] private Slider slider;

    private bool isSlider = false;

    void Start(){
        if (slider != null){
            isSlider = true;
            slider.maxValue = card.maxValue;
            slider.value = card.defaultvalue;
        }
        else{
            valueText.text = card.defaultvalue.ToString();
        }

        label.text = card.statName;

        if(icon != null) icon.texture = card.icon;
        if(backPanel != null) backPanel.texture = card.backPanel;
        if(valueBackground != null) valueBackground.texture = card.valueBackground;

    }
}
