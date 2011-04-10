###########################################################################
# anova kernel
###########################################################################
from tools.load import LoadMatrix
from numpy import double
lm=LoadMatrix()

traindat = double(lm.load_numbers('../data/fm_train_real.dat'))
testdat = double(lm.load_numbers('../data/fm_test_real.dat'))
parameter_list = [[traindat,testdat,2,10], [traindat,testdat,5,10]]

def kernel_anova_modular (fm_train_real=traindat,fm_test_real=testdat,cardinality=2, size_cache=10):
	from shogun.Kernel import ANOVAKernel
	from shogun.Features import RealFeatures
	
	feats_train=RealFeatures(fm_train_real)
	feats_test=RealFeatures(fm_test_real)
	
	
	kernel=ANOVAKernel(feats_train, feats_train, cardinality, size_cache)

	km_train=kernel.get_kernel_matrix()
	kernel.init(feats_train, feats_test)
	km_test=kernel.get_kernel_matrix()
	return km_train,km_test,kernel

if __name__=='__main__':
	print 'ANOVA'
	kernel_anova_modular(*parameter_list[0])
