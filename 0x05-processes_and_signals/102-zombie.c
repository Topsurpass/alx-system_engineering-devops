#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - An infinite loop
 *
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

/**
 * main - Entry point to the program
 *
 * Return: An infinite loop
 */
int main(void)
{
	pid_t zombie_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		/* Rtrn value of 0 indicates a child process has been created */
		if (zombie_pid == 0)
			exit(0);
		/* The parent returns the child's PID */
		else
			printf("Zombie process created, PID: %d\n", zombie_pid);
	}
	return (infinite_while());
}
