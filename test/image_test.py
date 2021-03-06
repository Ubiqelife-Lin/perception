"""
Tests the image class.
Author: Jeff Mahler
"""
from unittest import TestCase

import logging
import numpy as np

from constants import *

from perception import Image, ColorImage, DepthImage, BinaryImage, SegmentationImage, GrayscaleImage, IrImage, PointCloudImage, NormalCloudImage

class TestImage(TestCase):

    def test_color_init(self):
        # valid data
        random_valid_data = (255.0 * np.random.rand(IM_HEIGHT, IM_WIDTH, 3)).astype(np.uint8)
        im = ColorImage(random_valid_data)
        self.assertEqual(im.height, IM_HEIGHT)
        self.assertEqual(im.width, IM_WIDTH)
        self.assertEqual(im.channels, 3)
        self.assertTrue(np.allclose(im.data, random_valid_data))

        # invalid channels
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH).astype(np.uint8)
        caught_bad_channels = False
        try:
            im = ColorImage(random_data)
        except:
            caught_bad_channels = True
        self.assertTrue(caught_bad_channels)

        # invalid type
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH, 3).astype(np.float32)
        caught_bad_dtype = False
        try:
            im = ColorImage(random_data)
        except:
            caught_bad_dtype = True
        self.assertTrue(caught_bad_dtype)

    def test_depth_init(self):
        # valid data
        random_valid_data = np.random.rand(IM_HEIGHT, IM_WIDTH).astype(np.float32)
        im = DepthImage(random_valid_data)
        self.assertEqual(im.height, IM_HEIGHT)
        self.assertEqual(im.width, IM_WIDTH)
        self.assertEqual(im.channels, 1)
        self.assertEqual(im.type, np.float32)
        self.assertTrue(np.allclose(im.data, random_valid_data))

        # invalid channels
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH, 3).astype(np.float32)
        caught_bad_channels = False
        try:
            im = DepthImage(random_data)
        except:
            caught_bad_channels = True
        self.assertTrue(caught_bad_channels)

        # invalid type
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH).astype(np.uint8)
        caught_bad_dtype = False
        try:
            im = DepthImage(random_data)
        except:
            caught_bad_dtype = True
        self.assertTrue(caught_bad_dtype)

    def test_binary_init(self):
        # valid data
        random_valid_data = (255.0 * np.random.rand(IM_HEIGHT, IM_WIDTH)).astype(np.uint8)
        binary_data = 255 * (random_valid_data > 128)
        im = BinaryImage(random_valid_data)
        self.assertEqual(im.height, IM_HEIGHT)
        self.assertEqual(im.width, IM_WIDTH)
        self.assertEqual(im.channels, 1)
        self.assertTrue(np.allclose(im.data, binary_data))

        # invalid channels
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH, 3).astype(np.uint8)
        caught_bad_channels = False
        try:
            im = BinaryImage(random_data)
        except:
            caught_bad_channels = True
        self.assertTrue(caught_bad_channels)

        # invalid type
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH).astype(np.float32)
        caught_bad_dtype = False
        try:
            im = BinaryImage(random_data)
        except:
            caught_bad_dtype = True
        self.assertTrue(caught_bad_dtype)

    def test_grayscale_init(self):
        # valid data
        random_valid_data = (255.0 * np.random.rand(IM_HEIGHT, IM_WIDTH)).astype(np.uint8)
        im = GrayscaleImage(random_valid_data)
        self.assertEqual(im.height, IM_HEIGHT)
        self.assertEqual(im.width, IM_WIDTH)
        self.assertEqual(im.channels, 1)
        self.assertTrue(np.allclose(im.data, random_valid_data))

        # invalid channels
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH, 5).astype(np.uint8)
        caught_bad_channels = False
        try:
            im = GrayscaleImage(random_data)
        except:
            caught_bad_channels = True
        self.assertTrue(caught_bad_channels)

        # invalid type
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH).astype(np.float32)
        caught_bad_dtype = False
        try:
            im = GrayscaleImage(random_data)
        except:
            caught_bad_dtype = True
        self.assertTrue(caught_bad_dtype)

    def test_segment_init(self):
        # valid data
        random_valid_data = (255.0 * np.random.rand(IM_HEIGHT, IM_WIDTH)).astype(np.uint8)
        im = SegmentationImage(random_valid_data)
        self.assertEqual(im.height, IM_HEIGHT)
        self.assertEqual(im.width, IM_WIDTH)
        self.assertEqual(im.channels, 1)
        self.assertTrue(np.allclose(im.data, random_valid_data))

        # invalid channels
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH, 3).astype(np.uint8)
        caught_bad_channels = False
        try:
            im = SegmentationImage(random_data)
        except:
            caught_bad_channels = True
        self.assertTrue(caught_bad_channels)

        # invalid type
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH).astype(np.float32)
        caught_bad_dtype = False
        try:
            im = SegmentationImage(random_data)
        except:
            caught_bad_dtype = True
        self.assertTrue(caught_bad_dtype)

    def test_pc_init(self):
        # valid data
        random_valid_data = np.random.rand(IM_HEIGHT, IM_WIDTH, 3).astype(np.float32)
        im = PointCloudImage(random_valid_data)
        self.assertEqual(im.height, IM_HEIGHT)
        self.assertEqual(im.width, IM_WIDTH)
        self.assertEqual(im.channels, 3)
        self.assertTrue(np.allclose(im.data, random_valid_data))

        # invalid channels
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH).astype(np.float32)
        caught_bad_channels = False
        try:
            im = PointCloudImage(random_data)
        except:
            caught_bad_channels = True
        self.assertTrue(caught_bad_channels)

        # invalid type
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH, 3).astype(np.uint8)
        caught_bad_dtype = False
        try:
            im = PointCloudImage(random_data)
        except:
            caught_bad_dtype = True
        self.assertTrue(caught_bad_dtype)

    def test_nc_init(self):
        # valid data
        random_valid_data = np.random.rand(IM_HEIGHT, IM_WIDTH, 3).astype(np.float32)
        random_valid_data = random_valid_data / np.tile(np.linalg.norm(random_valid_data, axis=2)[:,:,np.newaxis], [1,1,3])
        im = NormalCloudImage(random_valid_data)
        self.assertEqual(im.height, IM_HEIGHT)
        self.assertEqual(im.width, IM_WIDTH)
        self.assertEqual(im.channels, 3)
        self.assertTrue(np.allclose(im.data, random_valid_data))

        # invalid channels
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH).astype(np.float32)
        caught_bad_channels = False
        try:
            im = NormalCloudImage(random_data)
        except:
            caught_bad_channels = True
        self.assertTrue(caught_bad_channels)

        # invalid type
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH, 3).astype(np.uint8)
        caught_bad_dtype = False
        try:
            im = NormalCloudImage(random_data)
        except:
            caught_bad_dtype = True
        self.assertTrue(caught_bad_dtype)

        # invalid norm
        random_data = np.random.rand(IM_HEIGHT, IM_WIDTH, 3).astype(np.float32)
        caught_bad_norm = False
        try:
            im = NormalCloudImage(random_data)
        except:
            caught_bad_norm = True
        self.assertTrue(caught_bad_norm)

    def test_resize(self):
        random_valid_data = (255.0 * np.random.rand(IM_HEIGHT, IM_WIDTH, 3)).astype(np.uint8)
        im = ColorImage(random_valid_data)

        big_scale = 2.0
        big_im = im.resize(big_scale)
        self.assertEqual(big_im.height, big_scale * IM_HEIGHT)
        self.assertEqual(big_im.width, big_scale * IM_WIDTH)

        small_scale = 0.5
        small_im = im.resize(small_scale)
        self.assertEqual(small_im.height, small_scale * IM_HEIGHT)
        self.assertEqual(small_im.width, small_scale * IM_WIDTH)

    def test_transform(self):
        random_valid_data = (255.0 * np.random.rand(IM_HEIGHT, IM_WIDTH, 3)).astype(np.uint8)
        im = ColorImage(random_valid_data)
        
        translation = np.array([2,2])
        im_tf = im.transform(translation, 0.0)
        self.assertTrue(np.allclose(im[0,0], im_tf[2,2]))

    def test_shape_comp(self):
        random_valid_data = (255.0 * np.random.rand(IM_HEIGHT, IM_WIDTH, 3)).astype(np.uint8)
        im1 = ColorImage(random_valid_data)
        random_valid_data = (255.0 * np.random.rand(IM_HEIGHT, IM_WIDTH, 3)).astype(np.uint8)
        im2 = ColorImage(random_valid_data)
        self.assertTrue(im1.is_same_shape(im2))

        random_valid_data = (255.0 * np.random.rand(2*IM_HEIGHT, 2*IM_WIDTH, 3)).astype(np.uint8)
        im3 = ColorImage(random_valid_data)        
        self.assertFalse(im1.is_same_shape(im3))        

    def test_mask_by_ind(self):
        random_valid_data = (255.0 * np.random.rand(IM_HEIGHT, IM_WIDTH, 3)).astype(np.uint8)
        im = ColorImage(random_valid_data)        

        ind = np.array([[0,0]])
        im2 = im.mask_by_ind(ind)
        self.assertEqual(np.sum(im2[1,1]), 0.0)

    def test_indexing(self, height=50, width=100):
        color_data = (255 * np.random.rand(height, width, 3)).astype(np.uint8)
        im = ColorImage(color_data, 'a')

        # test valid indexing on color images
        i = int(height * np.random.rand())
        j = int(width * np.random.rand())
        k = int(3 * np.random.rand())
        print
        logging.info('Indexing with i=%d, j=%d, k=%d' %(i, j, k))
        c_true = color_data[i,j,k]
        c_read = im[i,j,k]
        self.assertTrue(np.sum(np.abs(c_true - c_read)) < 1e-5, msg='Image ijk indexing failed')

        c_true = color_data[i,j,:]
        c_read = im[i,j]
        self.assertTrue(np.sum(np.abs(c_true - c_read)) < 1e-5, msg='Image ij indexing failed')

        c_true = color_data[i,:,:]
        c_read = im[i]
        self.assertTrue(np.sum(np.abs(c_true - c_read)) < 1e-5, msg='Image i indexing failed')

        # test out of bounds indexing on color image
        caught_out_of_bounds = False
        try:
            c_read = im[-1,j,k]
        except ValueError as e:
            caught_out_of_bounds = True
        self.assertTrue(caught_out_of_bounds)

        caught_out_of_bounds = False
        try:
            c_read = im[i,-1,k]
        except ValueError as e:
            caught_out_of_bounds = True
        self.assertTrue(caught_out_of_bounds)

        caught_out_of_bounds = False
        try:
            c_read = im[i,j,-1]
        except ValueError as e:
            caught_out_of_bounds = True
        self.assertTrue(caught_out_of_bounds)

        caught_out_of_bounds = False
        try:
            c_read = im[height,j,k]
        except ValueError as e:
            caught_out_of_bounds = True
        self.assertTrue(caught_out_of_bounds)

        caught_out_of_bounds = False
        try:
            c_read = im[i,width,k]
        except ValueError as e:
            caught_out_of_bounds = True
        self.assertTrue(caught_out_of_bounds)

        caught_out_of_bounds = False
        try:
            c_read = im[i,j,3]
        except ValueError as e:
            caught_out_of_bounds = True
        self.assertTrue(caught_out_of_bounds)

    def test_io(self, height=50, width=100):
        color_data = (255 * np.random.rand(height, width, 3)).astype(np.uint8)
        im = ColorImage(color_data, 'a')
        file_root = 'test/data/test_color'

        # save and load png
        filename = file_root + '.png'
        im.save(filename)
        loaded_im = ColorImage.open(filename)
        self.assertTrue(np.sum(np.abs(loaded_im.data - im.data)) < 1e-5, msg='ColorImage data changed after load png')

        # save and load jpg
        filename = file_root + '.jpg'
        im.save(filename)
        loaded_im = ColorImage.open(filename)

        # save and load npy
        filename = file_root + '.npy'
        im.save(filename)
        loaded_im = ColorImage.open(filename)
        self.assertTrue(np.sum(np.abs(loaded_im.data - im.data)) < 1e-5, msg='ColorImage data changed after load npy')

        # save and load npz
        filename = file_root + '.npz'
        im.save(filename)
        loaded_im = ColorImage.open(filename)
        self.assertTrue(np.sum(np.abs(loaded_im.data - im.data)) < 1e-5, msg='ColorImage data changed after load npz')

if __name__ == '__main__':
    unittest.main()
    
