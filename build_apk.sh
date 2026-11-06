#!/bin/bash
set -e

echo "=== BUILDING ANDROID APK FOR TÂNG! (BOUNCE IT!) ==="

SDK_ROOT="/home/nor/Android/Sdk"
BUILD_TOOLS="$SDK_ROOT/build-tools/35.0.0"
PLATFORM="$SDK_ROOT/platforms/android-35/android.jar"
PROJECT_DIR="/home/nor/Storage/Projects/TUẦN LỄ GAME HÀN QUỐC 2026/android_project"
OUTPUT_APK="/home/nor/Storage/Projects/TUẦN LỄ GAME HÀN QUỐC 2026/Tang_Bounce_It.apk"

rm -rf "$PROJECT_DIR"
mkdir -p "$PROJECT_DIR/src/com/kgw2026/tangbounceit"
mkdir -p "$PROJECT_DIR/res/values"
mkdir -p "$PROJECT_DIR/res/drawable"
mkdir -p "$PROJECT_DIR/assets"
mkdir -p "$PROJECT_DIR/bin"
mkdir -p "$PROJECT_DIR/gen"

# 1. AndroidManifest.xml
cat << 'MANIFEST' > "$PROJECT_DIR/AndroidManifest.xml"
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.kgw2026.tangbounceit"
    android:versionCode="1"
    android:versionName="1.0">

    <uses-sdk android:minSdkVersion="24" android:targetSdkVersion="35" />

    <application
        android:label="@string/app_name"
        android:icon="@drawable/icon"
        android:hardwareAccelerated="true"
        android:theme="@android:style/Theme.NoTitleBar.Fullscreen">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:configChanges="orientation|screenSize|keyboardHidden"
            android:screenOrientation="portrait">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
MANIFEST

# 2. strings.xml
cat << 'STRINGS' > "$PROJECT_DIR/res/values/strings.xml"
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">Tâng! (Bounce It!)</string>
</resources>
STRINGS

# 3. Create icon PNG
python3 -c "
from PIL import Image, ImageDraw
img = Image.new('RGBA', (192, 192), color=(230, 57, 70, 255))
d = ImageDraw.Draw(img)
d.ellipse([16, 16, 176, 176], fill=(255, 209, 102, 255), outline=(0, 119, 182, 255), width=8)
d.ellipse([70, 70, 122, 122], fill=(230, 57, 70, 255))
img.save('$PROJECT_DIR/res/drawable/icon.png')
"

# 4. Copy game web assets into assets/
cp "/home/nor/Storage/Projects/TUẦN LỄ GAME HÀN QUỐC 2026/prototype/index.html" "$PROJECT_DIR/assets/index.html"

# 5. MainActivity.java
cat << 'JAVA' > "$PROJECT_DIR/src/com/kgw2026/tangbounceit/MainActivity.java"
package com.kgw2026.tangbounceit;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);

        getWindow().getDecorView().setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_FULLSCREEN
                | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY);

        webView = new WebView(this);
        setContentView(webView);

        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setAllowFileAccess(true);
        settings.setAllowContentAccess(true);
        settings.setMediaPlaybackRequiresUserGesture(false);
        settings.setUseWideViewPort(true);
        settings.setLoadWithOverviewMode(true);

        webView.setWebViewClient(new WebViewClient());
        webView.setWebChromeClient(new WebChromeClient());

        webView.loadUrl("file:///android_asset/index.html");
    }

    @Override
    public void onBackPressed() {
        if (webView != null && webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
JAVA

echo "--- STEP 1: aapt package resources & generate R.java ---"
"$BUILD_TOOLS/aapt" package -f -m \
    -J "$PROJECT_DIR/gen" \
    -M "$PROJECT_DIR/AndroidManifest.xml" \
    -S "$PROJECT_DIR/res" \
    -I "$PLATFORM"

echo "--- STEP 2: compile Java classes ---"
javac --release 8 -cp "$PLATFORM" \
    -d "$PROJECT_DIR/bin" \
    "$PROJECT_DIR/gen/com/kgw2026/tangbounceit/R.java" \
    "$PROJECT_DIR/src/com/kgw2026/tangbounceit/MainActivity.java"

echo "--- STEP 3: convert to DEX via d8 (running inside bin to avoid space issues) ---"
cd "$PROJECT_DIR/bin"
CLASS_FILES=$(find . -name "*.class")
"$BUILD_TOOLS/d8" $CLASS_FILES --output .
cd - > /dev/null

echo "--- STEP 4: package APK with aapt ---"
"$BUILD_TOOLS/aapt" package -f \
    -M "$PROJECT_DIR/AndroidManifest.xml" \
    -S "$PROJECT_DIR/res" \
    -A "$PROJECT_DIR/assets" \
    -I "$PLATFORM" \
    -F "$PROJECT_DIR/bin/unaligned.apk"

# Add classes.dex into the unaligned apk
cd "$PROJECT_DIR/bin"
"$BUILD_TOOLS/aapt" add unaligned.apk classes.dex
cd - > /dev/null

echo "--- STEP 5: zipalign ---"
"$BUILD_TOOLS/zipalign" -f -p 4 "$PROJECT_DIR/bin/unaligned.apk" "$PROJECT_DIR/bin/aligned.apk"

echo "--- STEP 6: sign APK with debug keystore ---"
"$BUILD_TOOLS/apksigner" sign \
    --ks /home/nor/.android/debug.keystore \
    --ks-pass pass:android \
    --key-pass pass:android \
    --out "$OUTPUT_APK" \
    "$PROJECT_DIR/bin/aligned.apk"

echo "--- VERIFY SIGNED APK ---"
"$BUILD_TOOLS/apksigner" verify "$OUTPUT_APK"

ls -lh "$OUTPUT_APK"
echo "=== APK BUILD COMPLETE! ==="
