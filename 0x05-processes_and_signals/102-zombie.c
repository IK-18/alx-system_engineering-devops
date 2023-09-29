#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while - runs an infinite while loop
 *
 * Return: Nothing
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
 * main - main function
 *
 * Return: Always 0
 */
int main(void)
{
	pid_t pid;
	int i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			i++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
