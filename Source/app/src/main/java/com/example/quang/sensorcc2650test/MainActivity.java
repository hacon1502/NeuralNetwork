package com.example.quang.sensorcc2650test;

import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothGatt;
import android.bluetooth.BluetoothManager;
import android.bluetooth.le.ScanCallback;
import android.bluetooth.le.ScanResult;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private ListView mListDevice;
    private Button mButtonScan;
    private boolean mScanning = false;
    private boolean mBleSupported = true;
    private int mNumDevs = 0;
    private BleAdapter mBleAdapter;
    private static final int NO_DEVICE = -1;
    private BluetoothDevice mBluetoothDevice = null;
    private ArrayList<BleDeviceInfo> mDeviceInfoList = new ArrayList<>();
    private BluetoothAdapter mBtAdapter = null;
    private String[] mDeviceFilter = {"CC2650 SensorTag", "SensorTag2"};
    private BluetoothLeService mBluetoothLeService;
    private int mConnIndex = NO_DEVICE;
    private static BluetoothManager mBluetoothManager;
    private MainActivity mActivity = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        mActivity = this;
        setContentView(R.layout.activity_main);
        initView();
        mButtonScan.setOnClickListener(this);
        //startBluetoothLeService();
        mBluetoothLeService = BluetoothLeService.getInstance();
        mBluetoothManager = mBluetoothLeService.getBtManager();
        mBtAdapter = mBluetoothManager.getAdapter();
        if (mBtAdapter == null) {
            Toast.makeText(this, "Bluetooth not support", Toast.LENGTH_LONG).show();
            return;
        }
        mBleAdapter = new BleAdapter(this, mDeviceInfoList);
        mListDevice.setAdapter(mBleAdapter);
        mListDevice.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                // Toast.makeText(MainActivity.this, "Da click thanh cong", Toast.LENGTH_SHORT).show();
                mButtonScan.setEnabled(false);
                mBleAdapter.notifyDataSetChanged();
                onDeviceClick(position);

            }
        });
    }

    private void initView() {
        mListDevice = (ListView) findViewById(R.id.list_main_ble);
        mButtonScan = (Button) findViewById(R.id.button_main_scan);
    }

    @Override
    public void onClick(View v) {
        if (mScanning) {
            stopScan();
        } else {
            startScan();
        }
    }

    private void startScan() {
        if (mBleSupported) {
            mNumDevs = 0;
            mDeviceInfoList.clear();
            scanLeDevice(true);
        }
    }

    private void stopScan() {
    }

    private boolean scanLeDevice(boolean b) {
        if (b) {
            mBtAdapter.getBluetoothLeScanner().startScan(mLeScanCallback);
            mScanning = true;
        } else {
            mScanning = false;
            mBtAdapter.getBluetoothLeScanner().stopScan(mLeScanCallback);
        }
        return mScanning;
    }


    private ScanCallback mLeScanCallback = new ScanCallback() {
        @Override
        public void onScanResult(int callbackType, ScanResult result) {
            final BluetoothDevice device = result.getDevice();
            final int rssi = result.getRssi();
            runOnUiThread(new Runnable() {
                public void run() {
                    //  Filter devices
                    if (device.getName() != null) {
                        if (checkDeviceFilter(device.getName())) {
                            if (!deviceInfoExists(device.getAddress())) {
                                // New device doi tuong
                                BleDeviceInfo deviceInfo = createDeviceInfo(device, rssi);
                                addDevice(deviceInfo);
                            } else {
                                // Already in list, update RSSI info
                                BleDeviceInfo deviceInfo = findDeviceInfo(device);
                                deviceInfo.updateRssi(rssi);
                            }
                        }
                    }
                }

            });
        }
    };

    boolean checkDeviceFilter(String deviceAddr) {
        if (deviceAddr == null)
            return false;
        int n = mDeviceFilter.length;
        if (n > 0) {
            boolean found = false;
            for (int i = 0; i < n && !found; i++) {
                found = deviceAddr.contains(mDeviceFilter[i]);
            }
            return found;
        } else
            return true;
    }

    private boolean deviceInfoExists(String address) {
        for (int i = 0; i < mDeviceInfoList.size(); i++) {
            if (mDeviceInfoList.get(i).getBluetoothDevice().getAddress()
                    .equals(address)) {
                return true;
            }
        }
        return false;
    }

    // tao ble
    private BleDeviceInfo createDeviceInfo(BluetoothDevice device, int rssi) {
        BleDeviceInfo deviceInfo = new BleDeviceInfo(device, rssi);

        return deviceInfo;
    }

    // them ble
    private void addDevice(BleDeviceInfo device) {
        mNumDevs++;
        mDeviceInfoList.add(device);
        mBleAdapter.notifyDataSetChanged();

    }

    // tim ble
    private BleDeviceInfo findDeviceInfo(BluetoothDevice device) {
        for (int i = 0; i < mDeviceInfoList.size(); i++) {
            if (mDeviceInfoList.get(i).getBluetoothDevice().getAddress()
                    .equals(device.getAddress())) {
                return mDeviceInfoList.get(i);
            }
        }
        return null;
    }

    public void onDeviceClick(final int position) {
        Toast.makeText(this, "Da vao device", Toast.LENGTH_SHORT).show();
        if (mScanning)
            stopScan();


        mBluetoothDevice = mDeviceInfoList.get(position).getBluetoothDevice();
        if (mConnIndex == NO_DEVICE) {
            //connect
            mConnIndex = position;
            onConnect();
        } else {
            //dissconnect
            if (mConnIndex != NO_DEVICE) {
                mBluetoothLeService.disconnect(mBluetoothDevice.getAddress());
            }
        }
    }

    void onConnect() {
        if (mNumDevs > 0) {

            int connState = mBluetoothManager.getConnectionState(mBluetoothDevice,
                    BluetoothGatt.GATT);

            switch (connState) {
                case BluetoothGatt.STATE_CONNECTED:
                    mBluetoothLeService.disconnect(null);
                    break;
                case BluetoothGatt.STATE_DISCONNECTED:
                    boolean ok = mBluetoothLeService.connect(mBluetoothDevice.getAddress());
                    if (ok) {
                        Toast.makeText(mActivity,"Sensor has been connected",Toast.LENGTH_SHORT).show();
                    }
                    break;
                default:
                    // setError("Device busy (connecting/disconnecting)");
                    break;

            }
            //Toast.makeText(this, connState == BluetoothGatt.STATE_DISCONNECTED ? "Disconnected" : "Conected", Toast.LENGTH_SHORT).show();
        }
    }

}
