// Remember to fill in your name and student ID below.
char *yourName = "Shambhu ";
char *yourStudentID = "10677794";


// Part1) This function takes in a square sized grayscale image and applies thresholding on each pixel.
// Width and height of the image are equal to "dim".
void imageThresholding(unsigned char* image, int dim) {
	__asm {
		push ebx;
		push edi;
		push esi;

// YOUR CODE STARTS HERE
	// ElementAddress = BaseAddress + (ElementSizeInBytes * Offset)
	// Offset = (RowIndex * NumberOfColumns) + ColumnIndex

		//Code in C++
		/*
		int threshold = 0x80;
		int min = 0x00;
		int max = 0xFF;
		for (int i = 0; i < dim; ++i) {
			for (int j = 0; j < dim; ++j) {
				if (image[i][j] < threshold) {
					image[i][j] = min;
				}
				else {
					image[i][j] = max;
				}
			}
		}
		*/
		//Parameters
		mov eax, image
		//mov ebx, dim;

		mov edi, 0
		BEGIN_FOR_ROW:
			cmp edi, dim
			jge END_FOR_ROW
			mov esi, 0

			BEGIN_FOR_COL:
				cmp esi, dim
				jge END_FOR_COL
				mov ebx, 0 //Transfer row to ebx

				mov edx, 0 //Multiply row by dim (add row to row dim times)
				BEGIN_FOR_MUL:
					cmp edx, dim
					jge END_FOR_MUL
					add ebx, edi
					inc edx
					jmp BEGIN_FOR_MUL
				END_FOR_MUL:

				add ebx, esi
				xor edx, edx
				mov dl, [eax + ebx] 
				//mov ecx, 0x80000000
				mov cl, 0x80
				//and ecx, edx
				and cl, dl
				//cmp ecx, 0x00000000
				cmp cl, 0x00
				jne IF_HIGHER
				//cmp esi, 0x80
				//jae IF_HIGHER  //Instead of jge
				//mov [eax + ebx], 0x00
				xor edx, edx //set to Min
				jmp CONT
				IF_HIGHER:
					//Set to Max
					//mov esi, [eax + ebx]
					//mov edi, esi
					//xor edi, 0xFFFFFFFF
					//xor esi, edi
					or edx, 0xFFFFFFFF
					//mov [eax + ebx], 0xFF
				//xor [eax + ebx], 0xFFFFFFFF
				CONT:
					mov [eax + ebx], dl
					inc esi
					jmp BEGIN_FOR_COL

			END_FOR_COL:
				inc edi
				jmp BEGIN_FOR_ROW

		END_FOR_ROW: 
			mov image, eax
// YOUR CODE ENDS HERE
		
		pop esi;
		pop edi;
		pop ebx;
	}
	
}


