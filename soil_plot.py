import pandas as pd
import matplotlib.pyplot as plt

# Read data from the external text file 
#Spot_1 observations 
file_sekf = ''
file_ens = ''
file_obs = ''
# Replace 'path_to_your_file' with the actual path where your file is stored

# Read the data into a DataFrame
df_sekf = pd.read_csv(file_sekf)
df_obs = pd.read_csv(file_obs)
df_ens = pd.read_csv(file_ens)
#df = df.iloc[1::18]

# Convert 'DATETIME' column to datetime format
df['DATETIME'] = pd.to_datetime(df['DATETIME'])
df_sekf['DATETIME'] = pd.to_datetime(df_sekf['DATETIME'])
df_ens['DATETIME'] = pd.to_datetime(df_ens['DATETIME'])

figure, axis = plt.subplots(3, 2, figsize=(15,15))

#soil temperature
# axis[0,0].plot(df_ens['DATETIME'], df_ens['X002TG1'], label='TG1 ensrkf (-1 cm)', color='red')
# axis[0,0].plot(df_sekf['DATETIME'], df_sekf['X002TG1'], label='TG1 sEKF (-1 cm)', color='blue')
# axis[0,0].set_xlabel('Time')
# axis[0,0].set_ylabel('Temperature (K)')
# axis[0,0].legend()
# axis[0,0].grid()
# axis[0,0].tick_params(labelrotation=45)
# axis[0,0].set_ylim(272,295)

# axis[0,1].plot(df_ens['DATETIME'], df_ens['X002TG2'], label='TG2 ensrkf (-5 cm)', color='red')
# axis[0,1].plot(df_sekf['DATETIME'], df_sekf['X002TG2'], label='TG2 sEKF (-5 cm)', color='blue')
# axis[0,1].plot(df_obs['DATETIME'], df_obs['TS-5_spot1']+273.15, label='TS-5 obs', color='k')
# axis[0,1].set_xlabel('Time')
# axis[0,1].set_ylabel('Temperature (K)')
# axis[0,1].legend()
# axis[0,1].grid()
# axis[0,1].tick_params(labelrotation=45)
# axis[0,1].set_ylim(272,295)

# axis[1,0].plot(df_ens['DATETIME'], df_ens['X002TG3'], label='TG3 ensrkf (-10 cm)', color='red')
# axis[1,0].plot(df_sekf['DATETIME'], df_sekf['X002TG3'], label='TG3 sEKF (-10 cm)', color='blue')
# axis[1,0].plot(df_obs['DATETIME'], df_obs['TS-10_spot1']+273.15, label='TS-10 obs', color='k')
# axis[1,0].set_xlabel('Time')
# axis[1,0].set_ylabel('Temperature (K)')
# axis[1,0].legend()
# axis[1,0].grid()
# axis[1,0].tick_params(labelrotation=45)
# axis[1,0].set_ylim(272,295)

# axis[1,1].plot(df_ens['DATETIME'], df_ens['X002TG4'], label='TG4 ensrkf (-20 cm)', color='red')
# axis[1,1].plot(df_sekf['DATETIME'], df_sekf['X002TG4'], label='TG4 sEKF (-20 cm)', color='blue')
# axis[1,1].plot(df_obs['DATETIME'], df_obs['TS-20_spot1']+273.15, label='TS-20 obs', color='k')
# axis[1,1].set_xlabel('Time')
# axis[1,1].set_ylabel('Temperature (K)')
# axis[1,1].legend()
# axis[1,1].grid()
# axis[1,1].tick_params(labelrotation=45)
# axis[1,1].set_ylim(272,295)

# axis[2,0].plot(df_ens['DATETIME'], df_ens['X002TG5'], label='TG5 ensrkf (-40 cm)', color='red')
# axis[2,0].plot(df_sekf['DATETIME'], df_sekf['X002TG5'], label='TG5 sEKF (-40 cm)', color='blue')
# axis[2,0].plot(df_obs['DATETIME'], df_obs['TS-40_spot1']+273.15, label='TS-40 obs', color='k')
# axis[2,0].set_xlabel('Time')
# axis[2,0].set_ylabel('Temperature (K)')
# axis[2,0].legend()
# axis[2,0].grid()
# axis[2,0].tick_params(labelrotation=45)
# axis[2,0].set_ylim(272,295)

# axis[2,1].plot(df_ens['DATETIME'], df_ens['X002TG7'], label='TG7 ensrkf (-80 cm)', color='red')
# axis[2,1].plot(df_sekf['DATETIME'], df_sekf['X002TG7'], label='TG7 sEKF (-80 cm)', color='blue')
# axis[2,1].plot(df_obs['DATETIME'], df_obs['TS-80_spot1']+273.15, label='TS-80 obs', color='k')
# axis[2,1].set_xlabel('Time')
# axis[2,1].set_ylabel('Temperature (K)')
# axis[2,1].legend()
# axis[2,1].grid()
# axis[2,1].tick_params(labelrotation=45)
# axis[2,1].set_ylim(272,295)


##soil moisture
axis[0,0].plot(df_ens['DATETIME'], df_ens['X002WG1'], label='WG1 ensrkf (-1 cm)', color='red')
axis[0,0].plot(df_sekf['DATETIME'], df_sekf['X002WG1'], label='WG1 sEKF (-1 cm)', color='blue')
axis[0,0].set_xlabel('Time')
axis[0,0].set_ylabel('Soil moisture')
axis[0,0].legend()
axis[0,0].grid()
axis[0,0].tick_params(labelrotation=45)
axis[0,0].set_ylim(0.05,0.45)

axis[0,1].plot(df_ens['DATETIME'], df_ens['X002WG2'], label='WG2 ensrkf (-5 cm)', color='red')
axis[0,1].plot(df_sekf['DATETIME'], df_sekf['X002WG2'], label='WG2 sEKF (-5 cm)', color='blue')
axis[0,1].plot(df_obs['DATETIME'], df_obs['SM-5_spot1'], label='SM-5 obs', color='k')
axis[0,1].set_xlabel('Time')
axis[0,1].set_ylabel('Soil moisture')
axis[0,1].legend()
axis[0,1].grid()
axis[0,1].tick_params(labelrotation=45)
axis[0,1].set_ylim(0.05,0.45)

axis[1,0].plot(df_ens['DATETIME'], df_ens['X002WG3'], label='WG3 ensrkf (-10 cm)', color='red')
axis[1,0].plot(df_sekf['DATETIME'], df_sekf['X002WG3'], label='WG3 sEKF (-10 cm)', color='blue')
axis[1,0].plot(df_obs['DATETIME'], df_obs['SM-10_spot1'], label='SM-10 obs', color='k')
axis[1,0].set_xlabel('Time')
axis[1,0].set_ylabel('Soil moisture')
axis[1,0].legend()
axis[1,0].grid()
axis[1,0].tick_params(labelrotation=45)
axis[1,0].set_ylim(0.05,0.45)

axis[1,1].plot(df_ens['DATETIME'], df_ens['X002WG4'], label='WG4 ensrkf (-20 cm)', color='red')
axis[1,1].plot(df_sekf['DATETIME'], df_sekf['X002WG4'], label='WG4 sEKF (-20 cm)', color='blue')
axis[1,1].plot(df_obs['DATETIME'], df_obs['SM-20_spot1'], label='SM-20 obs', color='k')
axis[1,1].set_xlabel('Time')
axis[1,1].set_ylabel('Soil moisture')
axis[1,1].legend()
axis[1,1].grid()
axis[1,1].tick_params(labelrotation=45)
axis[1,1].set_ylim(0.05,0.45)

axis[2,0].plot(df_ens['DATETIME'], df_ens['X002WG5'], label='WG5 ensrkf (-40 cm)', color='red')
axis[2,0].plot(df_sekf['DATETIME'], df_sekf['X002WG5'], label='WG5 sEKF (-40 cm)', color='blue')
axis[2,0].plot(df_obs['DATETIME'], df_obs['SM-40_spot1'], label='SM-40 obs', color='k')
axis[2,0].set_xlabel('Time')
axis[2,0].set_ylabel('Soil moisture')
axis[2,0].legend()
axis[2,0].grid()
axis[2,0].tick_params(labelrotation=45)
axis[2,0].set_ylim(0.05,0.45)

axis[2,1].plot(df_ens['DATETIME'], df_ens['X002WG7'], label='WG7 ensrkf (-80 cm)', color='red')
axis[2,1].plot(df_sekf['DATETIME'], df_sekf['X002WG7'], label='WG7 sEKF (-80 cm)', color='blue')
axis[2,1].plot(df_obs['DATETIME'], df_obs['SM-80_spot1'], label='SM-80 obs', color='k')
axis[2,1].set_xlabel('Time')
axis[2,1].set_ylabel('Soil moisture')
axis[2,1].legend()
axis[2,1].grid()
axis[2,1].tick_params(labelrotation=45)
axis[2,1].set_ylim(0.05,0.45)

figure.suptitle("Model analysis (ICMSHANAL) compared to obs (Sodankylä station DIS0001)", fontsize=16)
figure.subplots_adjust(top=0.99)
figure.tight_layout()
plt.show()
