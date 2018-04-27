package com.example.quang.sensorcc2650test;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.List;

/**
 * Created by quang on 3/22/2018.
 */

public class BleAdapter extends ArrayAdapter<BleDeviceInfo> {
    private Context mContext;
    private LayoutInflater mLayoutInflater;
    private List<BleDeviceInfo> mBle;

    public BleAdapter(Context context, List<BleDeviceInfo> objects) {
        super(context, 0, objects);
        mContext = context;
        mBle = objects;
        mLayoutInflater = LayoutInflater.from(context);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {


        convertView = mLayoutInflater.inflate(R.layout.item_ble, parent, false);

        //findViewBId in convertView
        TextView tvDevice = (TextView) convertView.findViewById(R.id.text);
        TextView tvRssi = (TextView) convertView.findViewById(R.id.text_rssi);
        BleDeviceInfo ble = mBle.get(position);
        tvDevice.setText(ble.getBluetoothDevice().getAddress());
        tvRssi.setText(ble.getRssi()+ "dB");
        return convertView;
    }
}
