#include <iostream>

int main()
{
	int T; std::cin >> T;
	for (int test_case = 1; test_case <= T; test_case++)
	{
		int N; std::cin >> N;
		int factors[5] = { 2, 3, 5, 7, 11 };
		int answer[5] = {0, };

		for (int i = 0; i < 5; i++) 
		{
			while (N % factors[i] == 0 && N != 0)
			{
				answer[i]++;
				N /= factors[i];
			}
		}
		std::cout << '#' << test_case << ' ';
		for (int i = 0; i < 5; i++)
			std::cout << answer[i] << ' ';
		std::cout << '\n';

	}
	return 0;
}