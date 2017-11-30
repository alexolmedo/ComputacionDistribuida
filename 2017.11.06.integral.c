#include <stdio.h>
#include <math.h>
#include <omp.h>
//$ gcc 2017.11.06.hello.c -fopenmp -o hello

float calcularPi(double n){
  double integral = 0.0;
  #pragma omp parallel for reduction (+:integral)
  for (long i = 0; i <= 1000000; i++){
    integral += (4*(1/n))/(1+(i/n)*(i/n));
  }
  return integral;
}

float calcularPiSingle(double n){
  double integral = 0.0;
  for (long i = 0; i <= n; i++){
    integral += (4*(1/n))/(1+(i/n)*(i/n));
  }
  return integral;
}




int main() {
  double integral, single, n = 1000000;

  single = calcularPiSingle(n);
  printf("%.20f\n", single);

  integral = calcularPi(n);
  printf("%.20f\n", integral);

  return 0;
}
