package com.example.quang.sensorcc2650test;

import android.bluetooth.BluetoothDevice;

/**
 * Created by quang on 3/22/2018.
 */

public class BleDeviceInfo {
    private BluetoothDevice mBtDevice;
    private int mRssi;

    public BleDeviceInfo(BluetoothDevice device, int rssi) {
        mBtDevice = device;
        mRssi = rssi;
    }

    public BluetoothDevice getBluetoothDevice() {
        return mBtDevice;
    }

    public int getRssi() {
        return mRssi;
    }

    public void updateRssi(int rssiValue) {
        mRssi = rssiValue;
    }

}
