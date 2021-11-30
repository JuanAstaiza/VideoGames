using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class ControladorEscenas : MonoBehaviour
{
	public  GameObject canvasPerdiste;
	//private AudioSource SonidoDeSalto2;
    // Start is called before the first frame update
    void Start()
    {
		Time.timeScale = 1;
		//SonidoDeSalto2 = GetComponent<AudioSource>();
	
    }

    // Update is called once per frame
    void Update()
    {
        
    }

	public void Perdiste(){
		canvasPerdiste.SetActive(true);
		Time.timeScale=0;
		//SonidoDeSalto2.Play();
	}

	public void Reiniciar(){
		SceneManager.LoadScene(0);
	}
}
