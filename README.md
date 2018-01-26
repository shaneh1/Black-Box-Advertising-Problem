# Black-Box-Advertising-Problem
Original code supplied by Dr. James McDermott (UCD).
Solution submitted as part of coursework.
Hill-climbing, simulated annealing and iterated hill-climbing algorithms are applied to a black box advertising problem.
Goal of the algorithm is to find the optimal combination of venues to advertise at or not, occuring a cost at each advertising venue but also incurring penalties for failing to reach demographics. The program reads in data from the data files.
The algorithms cycle through different bitstring solutions in an attempt to find the combination with the lowest objective function value (defined as cost + penalties). Hyperparameters include max iterations, temperature and decay rate in simulated annealing, and restarts in iterated hill-climbing. Iterated hill-climbing works best on this particular dataset.
