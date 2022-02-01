package app.daazi.aluno.fipaye_wallet.view

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.*
import app.daazi.aluno.fipaye_wallet.R
import com.google.firebase.auth.ktx.auth
import com.google.firebase.ktx.Firebase

class SigninScreen : AppCompatActivity() {
    override fun onCreate(savedInstanceState : Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_signin_screen)

        onClickSignUp()
        btnActionSignIn()
        forgotThePassword()
        rememberMeCheck()
    }

    private fun rememberMeCheck() {
        TODO("Implement sharedPreferences to save user signin info")

    }

    private fun forgotThePassword() {}

    private fun btnActionSignIn() {
        val btnSignin = findViewById<Button>(R.id.btn_signin)
        val emailInput = findViewById<EditText>(R.id.emailOrPhoneInput)
        val passwordInput = findViewById<EditText>(R.id.passwordInput)

        btnSignin.setOnClickListener {
            if (emailInput.text.isEmpty() || passwordInput.text.isEmpty()){
                emailInput.error = "Digite o e-mail"
                passwordInput.error = "Digite a senha"
            }else{
                val intent = Intent(this, MainActivity::class.java)
                startActivity(intent)
            }
        }
    }

    private fun onClickSignUp() {
        val txtSignUp = findViewById<TextView>(R.id.signup_txt)
        txtSignUp.setOnClickListener {
            val intent = Intent(this, CreateAccountScreen::class.java)
            startActivity(intent)
        }

    }
}