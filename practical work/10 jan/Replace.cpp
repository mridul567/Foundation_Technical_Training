#include <stdio.h>
void prod(int a[], int n)
{ if (n == 0) {
 return;
 }
 int l[n], r[n];
 l[0] = 1;
 for (int i = 1; i < n; i++) {
 l[i] = a[i - 1] * l[i - 1];
 }
 r[n - 1] = 1;
 for (int j = n - 2; j >= 0; j--) {
 r[j] = a[j + 1] * r[j + 1];
 }
 for (int i = 0; i < n; i++) {
 a[i] = l[i] * r[i];
 }
}
int main() {
 int a[] = { 1, 3, 2, 4, 6, 5 };
 int n = sizeof(a) / sizeof(a[0]);
 prod(a, n);
 for (int i = 0; i < n; i++) {
 printf("%d ", a[i]);
 }
 return 0;
}