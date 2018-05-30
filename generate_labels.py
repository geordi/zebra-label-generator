import argparse
import os

DATA_DIR = 'data'


def print_stats(labels, no_input_files):
    print('Generated {} labels from {} files.'.format(labels, no_input_files))


def generate_label_in_epl_format(label):
    label_str = 'N\nA20,10,0,4,1,1,N,"room: {}"\nA20,50,0,4,1,1,N,"id: {}"\nA20,90,0,4,1,1,N,"sn: {}"\nP1'

    return label_str.format(label['room'], label['iid'], label['sn'])


def generate_labels_for_file(filename, room):
    labels = []
    with open(filename, 'rt') as f:
        for line in f:
            line = line.strip()
            if not line.startswith('#'):
                iid, _, name, sn, *_ = line.split(';')
                labels.append({'iid': iid, 'sn': sn, 'room': room})
    return labels


def generate_labels(directory, filenames, separate=False):
    no_labels = 0
    labels_all = []

    for filename in filenames:
        filename_with_dir = os.path.join(DATA_DIR, filename)
        room = filename.split('.')[0]

        labels = generate_labels_for_file(filename_with_dir, room.upper())
        labels = [generate_label_in_epl_format(label) for label in labels]
        labels_all.extend(labels)
        no_labels += len(labels)

        if separate:
            write_labels_to_file(labels, room + '.epl')

    if not separate:
        write_labels_to_file(labels_all, 'printable_labels.epl')

    return no_labels, len(filenames)


def write_labels_to_file(labels, filename):
    with open(filename, 'wt') as f:
        for label in labels:
            f.write(label)
            f.write('\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--separate', help='Create output labels in separate files according to input files', action='store_true')
    args = parser.parse_args()

    filenames = os.listdir(DATA_DIR)

    if args.separate:
        no_labels, no_input_files = generate_labels(DATA_DIR, filenames, separate=True)
    else:
        no_labels, no_input_files = generate_labels(DATA_DIR, filenames)

    print_stats(no_labels, no_input_files)

if __name__ == '__main__':
    main()

