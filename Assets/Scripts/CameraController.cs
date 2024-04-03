using UnityEngine;

public class CameraController : MonoBehaviour {

    [SerializeField] private float speed = 200f;
    [Range(0f, 1f)]

    [HideInInspector] public bool focus = false;
    [HideInInspector] public Vector3 posToFocus = Vector3.zero;

    private Vector3 movement = Vector3.zero;
    private Camera cam;

    void Awake(){
        cam = GetComponent<Camera>();
    }

    void GetInputs(){
        movement.Set(Input.GetAxisRaw("Horizontal"), Input.GetAxisRaw("Vertical"), 0f);
        movement.Normalize();
        if (Input.GetAxis("Mouse ScrollWheel") > 0f ) // forward
        {
            cam.orthographicSize--;
        }
        else if (Input.GetAxis("Mouse ScrollWheel") < 0f ) // backwards
        {
            cam.orthographicSize++;
        }
    }

    public void Focus(){
        transform.position = Vector3.Lerp(transform.position, posToFocus, 0.08f);
        cam.orthographicSize = Mathf.Lerp(cam.orthographicSize, 15, 0.08f);
    }

    void LateUpdate() {
        GetInputs();

        transform.position += movement * speed * Time.deltaTime;

        if(focus){
            if(Vector3.Distance(transform.position, posToFocus) > 0.04f){
                Focus();
            } 
            else{
                focus = false;
            }
        }
    }
}
