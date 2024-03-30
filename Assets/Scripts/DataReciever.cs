using System;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using TMPro;
using UnityEngine;

public class DataReciever : MonoBehaviour {

  private TcpClient socketConn;
  private Thread clientRecvThread;

  [SerializeField] private TMP_Text port1;

  [SerializeField] private string host = "localhost";
  [SerializeField] private int port = 65432;

  void Start() { ConnectToServer(); }

  void ConnectToServer() {
    try {
      clientRecvThread = new Thread(Listen);
      clientRecvThread.IsBackground = true;
      clientRecvThread.Start();
    } catch (Exception e) {
      Debug.Log("Cannot Connect due to: " + e);
    }
  }

  private string serverMsg = "0";
  void Listen() {
    try {
      socketConn = new TcpClient(host, port);
      Byte[] bytes = new Byte[1024];
      while (true) {
        using (NetworkStream stream = socketConn.GetStream()) {
          int length;
          while ((length = stream.Read(bytes, 0, bytes.Length)) != 0) {
            var incomingData = new byte[length];
            Array.Copy(bytes, 0, incomingData, 0, length);
            serverMsg = Encoding.ASCII.GetString(incomingData);

            // Decode message here

            // Send 'next' after receiving a message
            byte[] nextMessage = Encoding.ASCII.GetBytes("next");
            stream.Write(nextMessage, 0, nextMessage.Length);

            // Actually also send which element to send
            // Formatting: 01,05 <- Population number, state
          }
        }
      }
    } catch (SocketException e) {
      Debug.Log("Socket Exception " + e);
    }
  }

  // Update is called once per frame
  void Update() {
    if(port1 != null) port1.text = serverMsg;
  }
}
