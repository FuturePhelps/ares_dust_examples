import ares
import numpy as np
import matplotlib.pyplot as plt
from ares.physics.Constants import h, k_B, c, Lsun

# Setting the parameters
z = np.arange(4, 9, 1)

pars = ares.util.ParameterBundle('mirocha2020:univ')
pars['pop_dust_zmin'] = z[0]
pars['pop_dust_zmax'] = z[-1]
pars['pop_dust_Nz'] = len(z)

# Keep in mind this is in experimental mode
# If you want to see the self-consistent ARES model,
# set this parameter to False
pars['pop_dust_experimental'] = True

# Create a GalaxyEnsemble object and retrieve the DustPopulation object
pop = ares.populations.GalaxyPopulation(**pars)
dust = pop.dust

# Get M_star from the GalaxyEnsemble object at all redshifts
M_star = np.zeros((dust.Ngalaxies, dust.Nz))

for i in range(dust.Nz):
    M_star[:,i] = pop.get_field(dust.z[i], 'Ms')

# Retrieve the dust temperature from the DustPopulation object
T_dust = dust.T_dust

# Plot and save as pdf and png in the figures directory
fig, ax = plt.subplots(1,1)
fig.set_size_inches(6.5, 3.7)
for i in range(len(z)):
    ax.semilogx(M_star[:,i], T_dust[:,i], '.', label = r'$z=\;$' + ('%d' % z[i]))
ax.legend()
ax.set_title(r"Dust Temperature vs Stellar Mass")
ax.set_xlabel(r"$M_{\mathrm{star}}\;\;\left[M_\odot\right]$")
ax.set_ylabel(r"$T_{\mathrm{dust}}\;\;\left[\mathrm{K}\right]$")
fig.savefig("figures/Tdust_vs_Mstar.pdf", bbox_inches = 'tight')
fig.savefig("figures/Tdust_vs_Mstar.png", bbox_inches = 'tight')