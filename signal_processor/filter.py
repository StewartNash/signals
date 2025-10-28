# IIR Filter Design Procedure
# 1. Enter filter specifications
# 	a. Filter type: LP, HP, BP or BS
# 	b. Filter parameters
# 		i. LP, HP: Ap, As, fp, fs, F
# 			A. LP: (fp < fs), (F > 2*fs)
# 			B. HP: (fp > fs), (F > 2*fp)
# 		ii. BP, BS: Ap, As, fp1, fp2, fs1, fs2, F/2
# 			A. BP: (fs1 < fp1 < fp2 < fs2), (F > 2*fs2)
# 			B. BS: (fp1 < fs1 < fs2 < fp2), (F > 2*fp2) 
# 2. Compute filter order, N (table 4.4)
# 3. Compute analog LP zeros
# 4. Compute analog LP poles
# 5. Compute digital poles and zeros
# 6. Compute second order section coefficients
# 7. Format coefficients as a function of section index, k
# 8. Compute coefficients B1,k for odd first-order section (N-odd only)
# 9. Determine second order section normalization coefficients

#TODO: Create a Filter class which encapsulates all filter parameters
