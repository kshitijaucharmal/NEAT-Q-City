using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;

[CustomEditor(typeof(GridSystem))]
public class GridSystemEditor : Editor {
  public override void OnInspectorGUI() {
    base.OnInspectorGUI();
    GridSystem myTarget = (GridSystem)target;

    // Generate base
    if (GUILayout.Button("Generate Base")) {
      myTarget.GenerateBase();
    }

    // Generate base
    if (GUILayout.Button("Place Building")) {
      myTarget.Place(myTarget.buildingToPlace);
    }
    if (GUILayout.Button("Clean")) {
      myTarget.Clean();
    }
  }
}
