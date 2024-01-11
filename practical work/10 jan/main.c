#include <stdio.h>
void pair(int a[], int n, int s)
{
 for (int i = 0; i < n - 1; i++)
 {
 for (int j = i + 1; j < n; j++)
 {
 if (a[i] + a[j] == s)
 {
 printf("Pair found (%d, %d)\n", a[i], a[j]);
 return;
 }
 }
 }
 printf("Pair not found");
}
int main()
{
 int a[] = { 8, 9, 3, 6, 1};
 int s = 11;
 int n = sizeof(a)/sizeof(a[0]);
 pair(a, n, s);
 return 0;
}