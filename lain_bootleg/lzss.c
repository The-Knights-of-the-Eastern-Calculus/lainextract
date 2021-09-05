/* LZSS decompression code from lain bootleg, modified output from ghidra so
 * there are basically no actual variable names because I can't be bothered,
 * so good luck trying to actually read this code! */
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *LZSS_compressed_data;
char DAT_00412fbc;
int DAT_00412fbd;
char *LZSS_Output_Memory;
int DAT_00412fe0;
char DAT_0040d098[8] = {0x80, 0x40, 0x20, 0x10, 0x8, 0x4, 0x2, 0x1};
unsigned int DAT_00412fc8;
unsigned int DAT_00412fcc;
unsigned int DAT_00412fd0;
unsigned int DAT_00412fc4;
unsigned int DAT_00412fd4;
unsigned int DAT_00412fdc;
char *LZSS_unknown_array;

void FUN_00404a20(char *compressed_data)

{
  LZSS_compressed_data = compressed_data;
  DAT_00412fbc = 0;
  DAT_00412fbd = 0;
  return;
}

void FUN_00404ac0(char *output_memory)

{
  LZSS_Output_Memory = output_memory;
  DAT_00412fe0 = 0;
  return;
}

bool FUN_00404a70(void)

{
  int uVar1;

  if (DAT_00412fbd == 0) {
    DAT_00412fbc = *LZSS_compressed_data;
    LZSS_compressed_data = LZSS_compressed_data + 1;
  }
  uVar1 = DAT_00412fbd;
  DAT_00412fbd += 1;
  if (DAT_00412fbd == 0x8) {
    DAT_00412fbd = 0x0;
  }
  return (DAT_0040d098[uVar1] & DAT_00412fbc) != 0;
}

unsigned int FUN_00404a40(int param_1)

{
  bool bVar1;
  unsigned int uVar2;

  uVar2 = 0;
  if (param_1 != 0) {
    do {
      uVar2 <<= 1;
      bVar1 = FUN_00404a70();
      if (bVar1 != 0) {
        uVar2 |= 1;
      }
      param_1 += -1;
    } while (param_1 != 0);
  }
  return uVar2;
}

char *FUN_00404a00(unsigned int param_1)

{
  printf("FUN_00404a00 - param_1 = %i, offset = 0x%x\n", param_1, (DAT_00412fd0 - 1 & param_1));
  return (char *)((DAT_00412fd0 - 1 & param_1) + LZSS_unknown_array);
}

void FUN_00404b60(int param_1, char param_2)

{
  printf("FUN_00404b60 - param_1=%i, param_2=0x%x\n", param_1, param_2);
  if (param_1 != 0) {
    do {
      *LZSS_Output_Memory = param_2;
      LZSS_Output_Memory = LZSS_Output_Memory + 1;
      param_1 += -1;
    } while (param_1 != 0);
  }
  return;
}

void FUN_00404ae0(int param_1)

{
  if (DAT_00412fe0 == 0) {
    DAT_00412fdc = param_1;
    DAT_00412fe0 = 1;
    return;
  }
  if (DAT_00412fe0 != 1) {
    if (DAT_00412fe0 == 2) {
      DAT_00412fe0 = param_1;
      if (param_1 == 0) {
        DAT_00412fe0 = 0x100;
      }
      param_1 = DAT_00412fdc;
      if (3 < DAT_00412fe0) {
        return;
      }
    }
    FUN_00404b60(DAT_00412fe0, (char)param_1);
    DAT_00412fe0 = 1;
    return;
  }
  if (param_1 != DAT_00412fdc) {
    FUN_00404b60(1, (char)param_1);
    return;
  }
  DAT_00412fe0 = 2;
  return;
}

int FUN_00404950(void)

{
  bool bVar1;
  unsigned int uVar2;
  int iVar3;

  uVar2 = FUN_00404a40(DAT_00412fc8 - 1);
  if (DAT_00412fd4 - 1 <= (int)uVar2) {
    iVar3 = uVar2 * 2;
    bVar1 = FUN_00404a70();
    if (bVar1 != 0) {
      iVar3 += 1;
    }
    if (iVar3 == DAT_00412fd0 - 1) {
      return -1;
    }
    uVar2 = iVar3 + (1 - DAT_00412fd4);
  }
  return uVar2;
}

int FUN_00404900(void)

{
  bool bVar1;
  unsigned int uVar2;
  int iVar3;

  uVar2 = FUN_00404a40(DAT_00412fcc - 1);
  if (uVar2 == 1) {
    return 2;
  }
  iVar3 = uVar2 * 2;
  bVar1 = FUN_00404a70();
  if (bVar1 != 0) {
    iVar3 += 1;
  }
  if (iVar3 == 1) {
    iVar3 = 3;
  }
  if (iVar3 == 0) {
    iVar3 = DAT_00412fd4;
  }
  return iVar3;
}

void FUN_004049a0(int param_1, int param_2)

{
  char *bVar1;
  unsigned int uVar2;
  char *pbVar3;

  if (param_1 != 0) {
    do {
      pbVar3 = FUN_00404a00(param_2 + DAT_00412fc4);
      uVar2 = DAT_00412fc4;
      bVar1 = pbVar3;
      DAT_00412fc4 += 1;
      pbVar3 = FUN_00404a00(uVar2);
      pbVar3 = bVar1;
      FUN_00404ae0(*bVar1);
      param_1 += -1;
    } while (param_1 != 0);
  }
  return;
}

void DecompressLZSS(char *compressed_data, char *output_memory,
                    void *unknown_array)

{
  unsigned int uVar1;
  bool bVar2;
  unsigned int uVar3;
  char *puVar4;
  int iVar5;
  int iVar6;

  FUN_00404a20(compressed_data + 8);
  FUN_00404ac0(output_memory);
  DAT_00412fc8 = FUN_00404a40(5);
  printf("DAT_00412fc8 = %i\n", DAT_00412fc8);
  DAT_00412fcc = FUN_00404a40(4);
  printf("DAT_00412fcc = %i\n", DAT_00412fcc);
  DAT_00412fd0 = 1 << ((unsigned char)DAT_00412fc8 & 0x1f);
  printf("DAT_00412fd0 = %i\n", DAT_00412fd0);
  LZSS_unknown_array = unknown_array;
  DAT_00412fc4 = 0;
  DAT_00412fd4 = 1 << ((unsigned char)DAT_00412fcc & 0x1f);
  printf("DAT_00412fd4 = %i\n", DAT_00412fd4);
  do {
    bVar2 = FUN_00404a70();
    if (bVar2 == 0) {
      iVar5 = FUN_00404950();
      printf("iVar5 = %i\n", iVar5);
      if (iVar5 == -1) {
        return;
      }
      iVar6 = (DAT_00412fd0 - iVar5) + -1;
      printf("iVar6 = %i\n", iVar6);
      iVar5 = FUN_00404900();
      printf("iVar5 = %i\n", iVar5);
      FUN_004049a0(iVar5, iVar6);
    } else {
      uVar3 = FUN_00404a40(8);
      uVar1 = DAT_00412fc4;
      DAT_00412fc4 += 1;
      puVar4 = FUN_00404a00(uVar1);
      printf("puVar4 = %p, uVar3 = 0x%x\n", puVar4, uVar3);
      *puVar4 = (char)uVar3;
      FUN_00404ae0(uVar3);
    }
    DAT_00412fc4 &= DAT_00412fd0 - 1U;
  } while (true);
}

int load_file_to_memory(const char *filename, char **result) {
  int size = 0;
  FILE *f = fopen(filename, "rb");
  if (f == NULL) {
    *result = NULL;
    return -1; // -1 means file opening fail
  }
  fseek(f, 0, SEEK_END);
  size = ftell(f);
  fseek(f, 0, SEEK_SET);
  *result = (char *)malloc(size + 1);
  if (size != fread(*result, sizeof(char), size, f)) {
    free(*result);
    return -2; // -2 means file reading fail
  }
  fclose(f);
  (*result)[size] = 0;
  return size;
}

int main(int argc, char *argv[]) {
  if (argc != 4) {
    printf("Too many or too few arguments\nUsage: lzss in_filename "
           "out_filename\n");
    return 1;
  }

  char *compressed_data;
  char *uncompressed_data;
  int file_size;
  uint32_t uncompressed_size;

  file_size = load_file_to_memory(argv[1], &compressed_data);
  if (file_size < 0) {
    printf("Error loading input file\n");
    return 1;
  }

  if (memcmp(compressed_data, "LZSS", 4) != 0) {
    printf("Not a valid LZSS file");
    return 1;
  }

  uncompressed_size = *(uint32_t *)&compressed_data[4];
  printf("uncompressed_size: %d\n", uncompressed_size);
  uncompressed_data = (char *)malloc(uncompressed_size);
  void *unknown_array = malloc(65536);

  DecompressLZSS(compressed_data, uncompressed_data, unknown_array);
  FILE *f = fopen(argv[2], "wb");
  if (f == NULL) {
    printf("failed to open output file\n");
    return 1;
  }
  fwrite(uncompressed_data, uncompressed_size, 1, f);
  fclose(f);
  FILE *fp = fopen(argv[3], "wb");
  if (fp == NULL) {
    printf("failed to open output file\n");
    return 1;
  }
  fwrite(unknown_array, 65536, 1, fp);
  fclose(fp);
  return 0;
}
