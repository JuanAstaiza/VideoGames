//Librerias
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Character : MonoBehaviour
{
	// Start is called before the first frame update
	//void no retorna nada

	private Rigidbody2D rb;
	public float speed = 1;

	public ControladorEscenas controladorEscena;


	void Start()
	{
		/* PROBAR
		int vidas=5;
		string name = "Juan";
		Debug.Log("Nombre: "+name);
		Debug.Log("Vidas: "+vidas);*/

		rb = GetComponent<Rigidbody2D>();
	}

	// Update is called once per frame
	//bucle contante
	void Update()
	{
		if (Input.GetMouseButtonDown(0)){
			rb.velocity = Vector2.up * speed;
		}

	}

	private void OnCollisionEnter2D(Collision2D collision){
		controladorEscena.Perdiste();
	}
}
