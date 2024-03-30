using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(DataReciever))]
public class DataRecieverEditor : Editor {
  public override void OnInspectorGUI() {
    base.OnInspectorGUI();
    DataReciever myTarget = (DataReciever)target;

    // if (GUILayout.Button("Send Message")) {
    //   myTarget.SendMessage();
    // }

  }
}
