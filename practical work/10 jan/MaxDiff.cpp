#include <iostream>
int maxDiff(int a[], int n) 
 {
 int max = a[1] - a[0];
 int i, j;
 for (i = 0; i < n; i++) 
 {
 for (j = i + 1; j < n; j++) 
 {
 if (a[j] - a[i] > max)
 max = a[j] - a[i];
 }
 }
 return max;
 }
int main()
{
 int arr[] = {2, 7, 9, 5, 1,3,5};
 int n = sizeof(arr) / sizeof(arr[0]);
 std::cout << "Maximum difference is " << maxDiff(arr, n);
 return 0;
}
