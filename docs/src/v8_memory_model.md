# V8 memory model

## Isolate allocator

An `Isolate` has an `IsolateAllocator`. An `IsolateAllocator` has a
`PageAllocator`, which is used when allocating V8 heap pages.

## Heap::ConfigureHeap()

max_semi_space_size_ = 8 * (kSystemPointerSize / 4) * MB

max_old_generation_size = 700ul * (kSystemPointerSize / 4) * MB

## Outline

Heap
  - MemoryAllocator
    - data_page_allocator
    - code_page_allocator

## Heap memory allocator
