package app.daazi.aluno.fipaye_wallet.view

import android.annotation.SuppressLint
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import app.daazi.aluno.fipaye_wallet.R

@SuppressLint("CustomSplashScreen")
class SplashActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState : Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        buttonAction()
    }

    private fun buttonAction() {
        val btnSignin = findViewById<Button>(R.id.btn_signin)
        val btnCreateAccount = findViewById<Button>(R.id.btn_create)

        btnSignin.setOnClickListener {
            val intent = Intent(this, SigninScreen::class.java)
            startActivity(intent)
        }
        btnCreateAccount.setOnClickListener {
            val intent = Intent(this, CreateAccountScreen::class.java)
            startActivity(intent)
        }
    }
}