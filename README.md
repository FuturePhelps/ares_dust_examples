A collection of example codes to use the felix_dust ARES branch
containing galactic dust simulation code.

Keep in mind that this code is currently unfinished and that its current
dust model does not seem to match the ALPINE survey data,
and therefore should not be used to make any predictions yet.

ADDED PARAMETERS

This is a list of all the new parameters in this branch which are
not present in the other ARES branches. They are described below:

'pop_dust_fmin': minimum frequency (Hz) to analyze galactic dust 
		(default = 1e14)

'pop_dust_fmax': maximum frequency (Hz) to analyze galactic dust
		(default = 1e17)

'pop_dust_Nfreqs': number of frequencies between 'pop_dust_fmin'
		and 'pop_dust_fmax' to be sampled (default = 500)

'pop_dust_zmin': minimum redshift to analyze galactic dust
		(default = 4)

'pop_dust_zmax': maximum redshift to analyze galactic dust
		(default = 10)

'pop_dust_Nz': number of redshifts between 'pop_dust_zmin'
		and 'pop_dust_zmax' to be sampled (default = 7)

'pop_dust_distrib': values either 'homogeneous' or 'pt src'.
		If non-existent, defaults to 'homogeneous'.
		Used in the Imara et al. (2018) model for stars
		in a homogeneous spherical distribution or a
		point source distribution in the galaxy.

'pop_dust_experimental': values either True or False. If non-existent,
		defaults to False. If False, uses the self-consistent
		ARES data as input for the Imara model.
		If True, enables currently potentially unstable code
		which doesn't use the self-consistent ARES data.

		Currently, this means that the dust temperature is given
		by a log-linear parametrization instead of the Imara model.
		(there is also some other different code, notably the dust
		mass which is calculated from the Imara model).

		/!\            This part needs a lot of work            /!\