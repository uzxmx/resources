package org.example.bind;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

import hello.Hello;

public class MainActivity extends Activity {

    private TextView mTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mTextView = (TextView) findViewById(R.id.mytextview);

        // Call Go function.
        String greetings = Hello.greetings("Android and Gopher");
        mTextView.setText(greetings);
    }
}
