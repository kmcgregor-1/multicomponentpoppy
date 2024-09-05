import numpy as np
import json
import os

class MulticomponentPopulation:
    def __init__(self):
        self.n_bursts = 100  # Default number of points

    def set_number_of_points(self, n_bursts):
        """
        Set the number of random points to generate.

        Parameters:
        - n_points (int): Number of random points to generate.
        """
        self.n_bursts = n_bursts
    
    def multicomponent_init(self):
        """
        Initializes each event to have some number of simulated components.

        returns:
        - events_dict_array (array): array of initialized event parameter dicts.
        """

        events_dict_array = self._assign_num_components()

        return events_dict_array

    def build_multicomponent_pop(self, events_dict_array):
        """
        Builds a multicomponent population using various input parameter functions.

        returns:
        - events_dict_array (array): array of initialized event parameter dicts.
        """

        for event in events_dict_array:
            event = self._assign_arrival_time(event)
            event = self._assign_amplitude(event)
            event = self._assign_burst_width(event)
            event = self._assign_dm(event)
            event = self._assign_dm_index(event)
            event = self._assign_ref_freq(event)
            event = self._assign_scattering_index(event)
            event = self._assign_scattering_timescale(event)
            event = self._assign_spectral_index(event)
            event = self._assign_spectral_running(event)

        return events_dict_array

    def _assign_num_components(self):
        """
        Assigns the number of components for each burst using a poisson pmf

        returns:
        - events_dict_array (array): array of initialized event parameter dicts.
        """
        components_array_all = np.random.randint(1, 5, size = self.n_bursts)

        events_dict_array = []
        for i in range(self.n_bursts):
            event = {"num_components":int(components_array_all[i])}
            events_dict_array.append(event)

        return events_dict_array

    ###NOTE:: the following assign functions work differently than _assign_num_components !!!

    def _assign_arrival_time(self, dict):
        """
        Assigns the arrival time using a gaussian about the center time (arbitrary)

        returns:
        - dict (dict): dict of event with arrival time(s).
        """
        num_components = dict["num_components"]

        dict["arrival_time"] = list(np.random.normal(loc = 50., scale = 10., size = num_components))

        return dict
    
    def _assign_burst_width(self, dict):
        """
        Assigns the arrival time using a gaussian about the center time (arbitrary)

        returns:
        - dict (dict): dict of event with arrival time(s).
        """
        num_components = dict["num_components"]

        dict["burst_width"] = list(np.abs(np.random.normal(loc = 1, scale = 0.1, size = num_components)))

        return dict

    def _assign_amplitude(self, dict):
        """
        Assigns the amplitude to 1 for all components

        returns:
        - dict (dict): dict of event with arrival time(s).
        """
        num_components = dict["num_components"]

        dict["amplitude"] = list(np.zeros(num_components) + 1)

        return dict

    def _assign_dm(self, dict):
        """
        Assigns the dm to 450 for all components

        returns:
        - dict (dict): dict of event with dm(s).
        """
        num_components = dict["num_components"]

        dict["dm"] = list(np.zeros(num_components) + 450)

        return dict   

    def _assign_dm_index(self, dict):
        """
        Assigns the dm index to -2 for all components

        returns:
        - dict (dict): dict of event with dm(s).
        """
        num_components = dict["num_components"]

        dict["dm_index"] = list(np.zeros(num_components) - 2.)

        return dict     

    def _assign_ref_freq(self, dict):
        """
        Assigns the ref_freq to 600 for all components

        returns:
        - dict (dict): dict of event with ref_freq(s).
        """
        num_components = dict["num_components"]

        dict["ref_freq"] = list(np.zeros(num_components) + 600)

        return dict      

    def _assign_scattering_index(self, dict):
        """
        Assigns the scat_index to 1 for all components

        returns:
        - dict (dict): dict of event with scat_index(s).
        """
        num_components = dict["num_components"]

        dict["scattering_index"] = list(np.zeros(num_components) + 1.)

        return dict      

    def _assign_scattering_timescale(self, dict):
        """
        Assigns the scat_timescale to 0 for all components

        returns:
        - dict (dict): dict of event with scat_timescale(s).
        """
        num_components = dict["num_components"]

        dict["scattering_timescale"] = list(np.zeros(num_components))

        return dict     

    def _assign_spectral_index(self, dict):
        """
        Assigns the spectral_index to 10 for all components

        returns:
        - dict (dict): dict of event with spectral_index(s).
        """
        num_components = dict["num_components"]

        dict["spectral_index"] = list(np.zeros(num_components) + 10.)

        return dict      

    def _assign_spectral_running(self, dict):
        """
        Assigns the spectral_running to -100 for all components

        returns:
        - dict (dict): dict of event with spectral_running(s).
        """
        num_components = dict["num_components"]

        dict["spectral_running"] = list(np.zeros(num_components) - 100.)

        return dict
    
    def write_to_json(self, events_dict_array, output_dir, filename):
        """
        Write the generated points dictionary to a JSON file.

        Parameters:
        - output_dir (str): Directory to save the output file.
        - filename (str): Name of the output JSON file.
        """
        os.makedirs(output_dir, exist_ok=True)
        output_filename = os.path.join(output_dir, filename)

        with open(output_filename, 'w') as json_file:
            json.dump(events_dict_array, json_file, indent=4)

        print(f"Saved generated points to {output_filename}")
