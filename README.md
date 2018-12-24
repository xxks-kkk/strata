Enhance Strata with Lease
==================================

## Overview

In Strata paper, a lease mechnaism is described to facilitate file sharing across processes. However, it turns out that current Strata implementation does not have lease (researchers did do some experiments with file sharing across processes though). So, this project is to fill the gap. A side effect of this project is that with lease, Strata has some basic infrastructure to become a distributed file system like NFS.

## Setup

Follow the [Strata instruction](https://github.com/ut-osa/strata) to setup Strata.

The test program for Lease support is `libfs/tests/lease_test_driver.cc`. It 
will invoke `lease_test`, which is compiled from `libfs/tests/lease_test.cc`. 

The test suite is located under `libfs/tests/lease_test_suite/`. The instruction
on the format of `*.ini` can be seen by running `lease_test` binary.

If you see `f100M` anywhere in the test cases, run the following command to generate
a 100M file and named it as `f100M`:

```
dd if=/dev/urandom of=f100M bs=1048576 count=100
```
m
