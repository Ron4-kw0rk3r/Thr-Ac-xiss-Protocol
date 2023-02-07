
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

#include <string.h>

// tool  is section  installed 
void __ok_tools(char *name_tool) {
	
	char __vv[] = "[+]"; // True
	char __ff[] = "[-]"; // false 
	char PATH[100]; 
	sprintf(PATH, "/usr/bin/%s" , name_tool );
	// using access in unistd
	int __cptor = access(PATH, F_OK);

	if ( __cptor == 0 ) {

		printf("%s tool load [ %s ] \xA", __vv , name_tool );
		
	} else {
		printf("%s tool not found in system | find and install [ %s ] \xA", __ff , name_tool);
		
	}
	
}


void __db_tool() {
	char __vv[] = "[+]"; // True
	char __ff[] = "[-]"; // false 

	char __scount[100]; // set buff readding character line por line
	int linec = 0;
	char comm[100]; 
	char rest[100];

	// load file  in read 
	FILE *dbread = fopen("db_tools", "r");
	if ( dbread == NULL) {
		printf("Error: file error not read \xA");
		printf("DB: date base void...!\xA");
		//return 1;
		
	} else {
		printf("Load file: reading tools... \xA");
		//very complicate while read file   
		// sizeof longitud in file
		while ( fgets( __scount , sizeof( __scount ), dbread) != NULL) {
			//__ok_tools( __scount );
			//__ok_tools( __scount );
			sprintf(comm , "which %s", __scount);
			fscanf(popen(comm , "r"), "%s" , rest);
			if ( strcmp(rest, "") == 0 ) {
				printf("%s tool not found in system \xA ", __ff);		
				printf("find and install --x %s \xA", __scount);

			} else {

				printf("%s tool load  --> %s  \xA", __vv , __scount );	
				
			}
			
			linec++;
			//printf(">> %s \xA", __scount );
		// feets is function 
			//__ok_tools( __scount );
		}		
		printf(" DB date base information:\xA");
		printf(" Element size number line : %d \xA", linec);

		// for (int z = 1 ;fgets( __scount , sizeof( __scount ), dbread ); z++ ) {
			// __ok_tools( __scount );
			// fflush(stdout);
			// 
		// }

		fclose(dbread);
	}
	
}


int main() {

	printf("Reading tools in System");
	for ( int i = 0 ; i < 3 ; i ++ ) {
		printf(".");
		fflush(stdout);
		sleep(1);
		
	}
	printf("\xA");
	__db_tool();	/// comprobando que esta instalado las herramientas 
	// demo version
	//printf(">> %s \xA", __vv);
	
	return 0;
}
