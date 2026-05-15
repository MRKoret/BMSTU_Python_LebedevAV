; ModuleID = "js_compiler"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define i32 @"main"()
{
entry:
  %".2" = add i32 10, 20
  %".3" = bitcast [4 x i8]* @"fstr_1" to i8*
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".3", i32 %".2")
  %".5" = mul i32 10, 20
  %".6" = bitcast [4 x i8]* @"fstr_2" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %".5")
  ret i32 0
}

declare i32 @"printf"(i8* %".1", ...)

@"fstr_1" = internal constant [4 x i8] c"%d\0a\00"
@"fstr_2" = internal constant [4 x i8] c"%d\0a\00"