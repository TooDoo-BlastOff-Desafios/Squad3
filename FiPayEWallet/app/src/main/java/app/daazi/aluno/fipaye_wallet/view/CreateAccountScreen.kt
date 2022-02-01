package app.daazi.aluno.fipaye_wallet.view

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import app.daazi.aluno.fipaye_wallet.R
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

class CreateAccountScreen : AppCompatActivity() {

    override fun onCreate(savedInstanceState : Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_create_account)

        registerAction()
    }

    private fun registerAction() {
        val btnResigter = findViewById<Button>(R.id.register_btn)
        val emailInput = findViewById<EditText>(R.id.email_input)
        val passwordInput = findViewById<EditText>(R.id.password_input)

        btnResigter.setOnClickListener {
            if(emailInput.text.isEmpty() || emailInput.text == null || passwordInput.text.isEmpty() || passwordInput.text == null){
                emailInput.error = "Preencha o campo do email"
                passwordInput.error = "Preencha o campo da senha"
            } else{
                createUser()
            }
            TODO("Implement conditions to other input fields")
        }
    }

    private fun createUser() {
        val emailInput = findViewById<EditText>(R.id.email_input)
        val passwordInput = findViewById<EditText>(R.id.password_input)
        val authenticate = Firebase.auth

        authenticate.createUserWithEmailAndPassword(emailInput.text.toString(),passwordInput.text.toString())
            .addOnCompleteListener(this){
                Log.i("createUser", "createUser: Creatin Completed")
            }
            .addOnFailureListener(this){
                Log.e("createUser", "createUser: Failed to create UserData", )
            }

    }
}