# Learning C (Again) – For RDMA / RoCEv2 Network Testing in GPU DC Networks


This repo is my personal notebook and playground for (re)learning C — this time with a clear goal: to understand and test RDMA and RoCEv2 networking inside a GPU-heavy data center.

I’m not trying to become a C wizard. I just want to know enough to:

- Write basic RDMA send/write programs
- Understand what's happening under the hood in tools like `ib_write_bw`
- Debug packet loss or latency issues at the NIC level with confidence
- Connect it back to real GPU workloads running on things like Slurm or Kubernetes

If you’re also learning C from a systems/infra/devops perspective, please comment on resources you may know

## What I'm Trying to Learn

- How C talks to RDMA via `libibverbs` and `librdmacm`
- How to post sends and writes to a queue pair (QP)
- What rkeys and memory regions really are
- How RoCEv2 behaves under pressure (MTU, ECN, PFC)
- How to collect meaningful benchmarks in a GPU DC

## Build + Run

### apt packages

```bash
sudo apt install rdma-core libibverbs-dev librdmacm-dev
