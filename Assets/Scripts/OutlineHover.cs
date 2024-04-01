using UnityEngine;

public class OutlineHover : MonoBehaviour {

    public Outline outline;
    public MeshRenderer sr;
    public GameObject statsUI;

    private CameraController cam;

    void Start(){
        cam = FindObjectOfType<CameraController>();
        Toggle(false);
    }

    void OnMouseEnter(){
        Toggle(true);
    }

    void OnMouseOver(){
        // If clicked
        if(Input.GetMouseButtonDown(0)){
            cam.focus = true;
            Vector3 posToFocus = transform.position + new Vector3(-3,0, -3);
            posToFocus.y = 20;
            cam.posToFocus = posToFocus;
        }
    }

    void OnMouseExit(){
        Toggle(false);
    }

    void Toggle(bool b){
        sr.enabled = b;
        outline.enabled = b;
        statsUI.SetActive(b);
    }
}
