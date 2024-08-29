import pandas as pd
import matplotlib.pyplot as plt

# Read data from the external text file 
#Spot_1 observations 
file_sekf = 'model_data_sekf.txt'
file1 = 'combined_moisturetemp.txt'
# Replace 'path_to_your_file' with the actual path where your file is stored

# Read the data into a DataFrame
df_sekf = pd.read_csv(file_sekf)
df = pd.read_csv(file1)
#df = df.iloc[1::18]

# Convert 'DATETIME' column to datetime format
df['DATETIME'] = pd.to_datetime(df['DATETIME'])
df_sekf['DATETIME'] = pd.to_datetime(df_sekf['DATETIME'])

figure, axis = plt.subplots(3, 2, figsize=(15,15))

######soil temperature#######
# axis[0,0].plot(df['DATETIME'], df['X002TG1'], label='TG1 (-1 cm)', color='red')
# axis[0,0].plot(df_sekf['DATETIME'], df_sekf['X002TG1_sekf'], label='TG1 sEKF (-1 cm)', color='blue')
# axis[0,0].set_xlabel('Time')
# axis[0,0].set_ylabel('Temperature (K)')
# axis[0,0].legend()
# axis[0,0].grid()
# axis[0,0].tick_params(labelrotation=45)
# axis[0,0].set_ylim(272,295)

# axis[0,1].plot(df['DATETIME'], df['X002TG2'], label='TG2 (-5 cm)', color='red')
# axis[0,1].plot(df_sekf['DATETIME'], df_sekf['X002TG2_sekf'], label='TG2 sEKF (-5 cm)', color='blue')
# axis[0,1].plot(df['DATETIME'], df['TS-80_spot1']+273.15, label='TS-5 obs', color='k')
# axis[0,1].set_xlabel('Time')
# axis[0,1].set_ylabel('Temperature (K)')
# axis[0,1].legend()
# axis[0,1].grid()
# axis[0,1].tick_params(labelrotation=45)
# axis[0,1].set_ylim(272,295)

# axis[1,0].plot(df['DATETIME'], df['X002TG3'], label='TG3 (-10 cm)', color='red')
# axis[1,0].plot(df_sekf['DATETIME'], df_sekf['X002TG3_sekf'], label='TG3 sEKF (-10 cm)', color='blue')
# axis[1,0].plot(df['DATETIME'], df['TS-40_spot1']+273.15, label='TS-10 obs', color='k')
# axis[1,0].set_xlabel('Time')
# axis[1,0].set_ylabel('Temperature (K)')
# axis[1,0].legend()
# axis[1,0].grid()
# axis[1,0].tick_params(labelrotation=45)
# axis[1,0].set_ylim(272,295)

# axis[1,1].plot(df['DATETIME'], df['X002TG4'], label='TG4 (-20 cm)', color='red')
# axis[1,1].plot(df_sekf['DATETIME'], df_sekf['X002TG4_sekf'], label='TG4 sEKF (-20 cm)', color='blue')
# axis[1,1].plot(df['DATETIME'], df['TS-20_spot1']+273.15, label='TS-20 obs', color='k')
# axis[1,1].set_xlabel('Time')
# axis[1,1].set_ylabel('Temperature (K)')
# axis[1,1].legend()
# axis[1,1].grid()
# axis[1,1].tick_params(labelrotation=45)
# axis[1,1].set_ylim(272,295)

# axis[2,0].plot(df['DATETIME'], df['X002TG5'], label='TG5 (-40 cm)', color='red')
# axis[2,0].plot(df_sekf['DATETIME'], df_sekf['X002TG5_sekf'], label='TG5 sEKF (-40 cm)', color='blue')
# axis[2,0].plot(df['DATETIME'], df['TS-10_spot1']+273.15, label='TS-40 obs', color='k')
# axis[2,0].set_xlabel('Time')
# axis[2,0].set_ylabel('Temperature (K)')
# axis[2,0].legend()
# axis[2,0].grid()
# axis[2,0].tick_params(labelrotation=45)
# axis[2,0].set_ylim(272,295)

# axis[2,1].plot(df['DATETIME'], df['X002TG7'], label='TG7 (-80 cm)', color='red')
# axis[2,1].plot(df_sekf['DATETIME'], df_sekf['X002TG7_sekf'], label='TG7 sEKF (-80 cm)', color='blue')
# axis[2,1].plot(df['DATETIME'], df['TS-5_spot1']+273.15, label='TS-80 obs', color='k')
# axis[2,1].set_xlabel('Time')
# axis[2,1].set_ylabel('Temperature (K)')
# axis[2,1].legend()
# axis[2,1].grid()
# axis[2,1].tick_params(labelrotation=45)
# axis[2,1].set_ylim(272,295)


####soil moisture#####
axis[0,0].plot(df['DATETIME'], df['X002WG1'], label='WG1 (-1 cm)', color='red')
axis[0,0].plot(df_sekf['DATETIME'], df_sekf['X002WG1'], label='WG1 sEKF (-1 cm)', color='blue')
axis[0,0].set_xlabel('Time')
axis[0,0].set_ylabel('Soil moisture')
axis[0,0].legend()
axis[0,0].grid()
axis[0,0].tick_params(labelrotation=45)
axis[0,0].set_ylim(0.15,0.45)

axis[0,1].plot(df['DATETIME'], df['X002WG2'], label='WG2 (-5 cm)', color='red')
axis[0,1].plot(df_sekf['DATETIME'], df_sekf['X002WG2'], label='WG2 sEKF (-5 cm)', color='blue')
axis[0,1].plot(df['DATETIME'], df['SM-5_spot1'], label='SM-5 obs', color='k')
axis[0,1].set_xlabel('Time')
axis[0,1].set_ylabel('Soil moisture')
axis[0,1].legend()
axis[0,1].grid()
axis[0,1].tick_params(labelrotation=45)
axis[0,1].set_ylim(0.15,0.45)

axis[1,0].plot(df['DATETIME'], df['X002WG3'], label='WG3 (-10 cm)', color='red')
axis[1,0].plot(df_sekf['DATETIME'], df_sekf['X002WG3'], label='WG3 sEKF (-10 cm)', color='blue')
axis[1,0].plot(df['DATETIME'], df['SM-10_spot1'], label='SM-10 obs', color='k')
axis[1,0].set_xlabel('Time')
axis[1,0].set_ylabel('Soil moisture')
axis[1,0].legend()
axis[1,0].grid()
axis[1,0].tick_params(labelrotation=45)
axis[1,0].set_ylim(0.15,0.45)

axis[1,1].plot(df['DATETIME'], df['X002WG4'], label='WG4 (-20 cm)', color='red')
axis[1,1].plot(df_sekf['DATETIME'], df_sekf['X002WG4'], label='WG4 sEKF (-20 cm)', color='blue')
axis[1,1].plot(df['DATETIME'], df['SM-20_spot1'], label='SM-20 obs', color='k')
axis[1,1].set_xlabel('Time')
axis[1,1].set_ylabel('Soil moisture')
axis[1,1].legend()
axis[1,1].grid()
axis[1,1].tick_params(labelrotation=45)
axis[1,1].set_ylim(0.15,0.45)

axis[2,0].plot(df['DATETIME'], df['X002WG5'], label='WG5 (-40 cm)', color='red')
axis[2,0].plot(df_sekf['DATETIME'], df_sekf['X002WG5'], label='WG5 sEKF (-40 cm)', color='blue')
axis[2,0].plot(df['DATETIME'], df['SM-40_spot1'], label='SM-40 obs', color='k')
axis[2,0].set_xlabel('Time')
axis[2,0].set_ylabel('Soil moisture')
axis[2,0].legend()
axis[2,0].grid()
axis[2,0].tick_params(labelrotation=45)
axis[2,0].set_ylim(0.15,0.45)

axis[2,1].plot(df['DATETIME'], df['X002WG7'], label='WG7 (-80 cm)', color='red')
axis[2,1].plot(df_sekf['DATETIME'], df_sekf['X002WG7'], label='WG7 sEKF (-80 cm)', color='blue')
axis[2,1].plot(df['DATETIME'], df['SM-80_spot1'], label='SM-80 obs', color='k')
axis[2,1].set_xlabel('Time')
axis[2,1].set_ylabel('Soil moisture')
axis[2,1].legend()
axis[2,1].grid()
axis[2,1].tick_params(labelrotation=45)
axis[2,1].set_ylim(0.15,0.45)


###Show plot####
figure.suptitle("exp (cerise_ensrkf_v16Feb) compared to obs (station DIS0005)", fontsize=16)
figure.subplots_adjust(top=0.99)
figure.tight_layout()
plt.show()
