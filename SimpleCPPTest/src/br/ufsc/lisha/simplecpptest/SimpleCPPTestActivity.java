package br.ufsc.lisha.simplecpptest;

import android.app.Activity;
import android.os.Bundle;
import android.widget.TextView;

public class SimpleCPPTestActivity extends Activity {
	
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        TextView tv = new TextView(this);
        tv.setText(stringFromSimple());
        setContentView(tv);
    }
    
    /* A native method that is implemented by the
     * 'simple' native library.
     */
    public native String stringFromSimple();
    
    /* Lets load our C library
     */
    static {
        System.loadLibrary("simple");
    }
}
