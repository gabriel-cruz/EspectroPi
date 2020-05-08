import seabreeze.spectrometers as sb

devices = sb.list_devices()
spec = sb.Spectrometer(devices[0])

spec.integration_time_micros(12000)
wavelengthArray = spec.wavelengths()
intensityArray = spec.intensities()		
	
	
for x in range(0, len(wavelengthArray)):
	f.write(str(wavelengthArray[x]))
	f.write(',')
	f.write(str(intensityArray[x]))
	f.write('\n')

print("Spectrometer Data Collected")
