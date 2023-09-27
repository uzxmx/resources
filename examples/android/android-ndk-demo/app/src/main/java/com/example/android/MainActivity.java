package com.example.android;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.view.KeyEvent;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.example.android.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {

    static {
        System.loadLibrary("jnish");
        System.loadLibrary("main");
    }

    private ActivityMainBinding binding;

    private int value = 0;

    private boolean backKeyPressed = false;

    private Handler handler = new Handler();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Log.i("MainActivity", "onCreate");

        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        // Example of a call to a native method
        TextView tv = binding.sampleText;
        tv.setText(stringFromJNI());

        binding.btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                JNIUtils.staticNativeBar("foo", 1);
                JNIUtils utils = new JNIUtils();
                utils.nativeFoo();

                value = sum(value, 1);
                tv.setText(Integer.toString(value));
            }
        });

        binding.startBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(MainActivity.this, DetailsActivity.class));
            }
        });

        binding.btnFuncWithJString.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                JNIUtils utils = new JNIUtils();
                utils.funcWithJString("Hello world");
            }
        });
    }

    @Override
    protected void onResume() {
        super.onResume();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
    }

    /**
     * A native method that is implemented by the 'android' native library,
     * which is packaged with this application.
     */
    public native String stringFromJNI();

    public native int sum(int a, int b);

    @Override
    public boolean onKeyDown(int keyCode, KeyEvent event) {
        if (keyCode == KeyEvent.KEYCODE_BACK) {
            if (backKeyPressed) {
                System.exit(0);
            } else {
                backKeyPressed = true;
                Toast.makeText(this, "Press again to exit", Toast.LENGTH_LONG).show();
                handler.postDelayed(() -> {
                    backKeyPressed = false;
                }, 2000);
            }
            return true;
        }
        return super.onKeyDown(keyCode, event);
    }
}
