#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Entry point
 * Return: 0 success
 */

int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (!pid)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", pid);
	}
	infinite_while();
}

/**
 * infinite_while - runs forever
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
