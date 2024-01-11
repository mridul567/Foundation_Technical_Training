#include <iostream>
int firstNonRepeating(int arr[], int n)
{
 for (int i = 0; i < n; i++) {
 int j;
 for (j = 0; j < n; j++)
 if (i != j && arr[i] == arr[j])
 break;
 if (j == n)
 return arr[i];
 }
 return -1;
}
int main()
{
 int arr[] = {-1, 2, -1, 3, 0};
 int n = sizeof(arr) / sizeof(arr[0]);
 std::cout << firstNonRepeating(arr, n);
 return 0;
}