using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class StatCardManager : MonoBehaviour{

    public States state;

    private StatCard card;
    private StateManager sm;

    [SerializeField] private TMP_Text label;
    [SerializeField] private TMP_Text valueText;

    [Header("If Slider")]
    [SerializeField] private Slider slider;


    void Start(){
        sm = FindObjectOfType<StateManager>();
        card = sm.GetCard(state);

        label.text = card.state.ToString();
    }

    void SetValues(){
        if (slider != null){
            slider.maxValue = 1;
            slider.value = card.defaultvalue;
        }
        else{
            int val = (int)(card.defaultvalue * 100);
            valueText.text = val.ToString();
        }
    }

    void Update(){
        SetValues();
    }
}
