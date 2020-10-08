extern "C" {
#include "simulation.h"
#include "asv.h"
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "scene.h"
#include "constants.h"
#include <iostream>

using namespace asv_swarm;

int main(int argc, char** argv)
{
  if(argc != 6)
  {
    fprintf(stderr, 
      "Error. " 
      "Usage: %s in_file out_file sig_wave_ht(m) wave_heading(deg) rand_seed.\n", 
      argv[0]);
    return 1;
  }

  char* p_end; 
  char* in_file = argv[1];
  char* out_file = argv[2]; 
  double wave_height = strtod(argv[3], &p_end);
  double wave_heading = strtod(argv[4], &p_end);
  long rand_seed = strtol(argv[5], &p_end, 10);  

  // Set simulation inputs
  struct Simulation* simulation = simulation_new_node();
  simulation_set_input(simulation,
                       in_file, 
                       wave_height,
                       wave_heading,
                       rand_seed);

  // Create object to coordinate visualization
  Visualisation::Scene scene(simulation);

  // Start visualization 
  scene.start();

  return EXIT_SUCCESS;
}
