package reversebits

// ReverseBits returns n with all 32 bit positions reversed.
func ReverseBits(n uint32) uint32 {
	var reversed uint32
	for i := 0; i < 32; i++ {
		reversed = (reversed << 1) | (n & 1)
		n >>= 1
	}
	return reversed
}
