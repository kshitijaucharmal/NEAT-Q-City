using UnityEngine;

public class OutlineHover : MonoBehaviour {

    public Outline outline;
    public MeshRenderer sr;

    private CameraController cam;

    void Start(){
        cam = FindObjectOfType<CameraController>();
        sr.enabled = false;
        outline.enabled = false;
    }

    void OnMouseEnter(){
        sr.enabled = true;
        outline.enabled = true;

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
        sr.enabled = false;
        outline.enabled = false;
    }
}
